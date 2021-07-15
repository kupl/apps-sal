n = int(input())
s =0
l = list(map(int,input().split()))
for i in range(1,n+1):
    s = s+i
p = sum(l)
if(sum(l) == s):
    print("YES")
else:
    print("NO")
    

