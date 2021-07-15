import math
n=int(input())
ans=100
for a in range(1,int(math.sqrt(n))+1):
    if n%a==0:
        m=max(len(str(a)),len(str(n//a)))
        ans=min(ans,m)
print(ans)
