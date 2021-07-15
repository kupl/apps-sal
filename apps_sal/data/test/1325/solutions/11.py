import math
def min_dist(c1,c2):
    g = abs(ord(c1)-ord(c2))
    return(min(g,26-g))
        
length, p = [int(k) for k in input().split()]
s = str(input())
s = " " + s
mid = int(len(s)/2)
#print(mid)
if p > mid:
    p = len(s)  - p
#print(p)
diff = [0] *(length+1) #if position i different from length - i, then diff[i] = 1
for i in range(1,mid+1):
    #print(s[i], s[length-i +1])
    if s[i] != s[length - i +1]:
        diff[i] = 1
        diff[length-i+1] = 1
#print(diff)
left = 0
right = 0
for i in range(1,p):
    if diff[i]==1:
        left = p-i
        break
g = mid
if length % 2 ==1:
    g = g - 1
for i in range(g,p,-1):
    if diff[i] ==1:
        right = i-p
        break

#print(left,right)

if left >= right: #go right first
    horizontal = 2*right + left
else:
    horizontal = 2*left + right
    
vertical = 0
for i in range(1,mid+1):
    if diff[i] == 1:
        vertical += min_dist(s[i], s[length-i +1])
        #print(min_dist(s[i], s[length-i +1]))
print(horizontal + vertical)
