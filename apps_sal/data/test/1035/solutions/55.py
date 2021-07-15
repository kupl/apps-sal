import math

a,b=map(int,input().split())

n=math.gcd(a,b)

cnt=1

f=2
d=n
while f*f<=n:
    if d%f==0:
        cnt+=1
        while d%f==0:
            d=d//f
    f+=1
if d!=1:
    cnt+=1

print(cnt)
