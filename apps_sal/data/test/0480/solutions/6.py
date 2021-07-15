from sys import stdin

s,x1,x2=list(map(int,stdin.readline().split()))
t1,t2=list(map(int,stdin.readline().split()))
p,d=list(map(int,stdin.readline().split()))
#d=v*t t=d/v
if x1>=x2:
    x2,x1=s-x2,s-x1
    p=s-p
    d*=-1
tempsPied=(x2-x1)*t2

if d==-1:
    tempsTram=(p+x2)*t1
elif d==1 and p>x1:
    tempsTram=((s-p)+s+x2)*t1
else:
    tempsTram=(x2-p)*t1
print(min(tempsPied,tempsTram))

