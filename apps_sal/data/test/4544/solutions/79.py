n = int(input())
a = list(map(int,input().split()))
ans = 0
 
l = [0]*100001
 
for i in a:
  l[i] += 1

for i in range(len(l)-2):
  ans = max(ans,l[i]+l[i+1]+l[i+2])
  
print(ans)
