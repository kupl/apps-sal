import math
n,k=map(int,input().split())
p=math.ceil(n/(2*k + 1))
a=[]
t=max(1,k+1-(2*k +1 - n%(2*k + 1)) )
if n%(2*k + 1)==0:
    t=k+1
for i in range(p):
    a.append(t)
    t+=(2*k + 1)
print(p)
print(*a)
