import math
n=int(input())
ans=10
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        b=int(n/i)
        f=max(len(str(i)),len(str(b)))
        ans=min(f,ans)
print(ans)
