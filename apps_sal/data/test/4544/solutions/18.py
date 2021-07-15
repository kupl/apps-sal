import numpy as np
n=int(input())
a=np.array(sorted(map(int,input().split())))
d=np.array([0]*(10**5+3))
e=np.array([0]*(10**5+3))
f=np.array([0]*(10**5+3))
for i in a:
    d[i+1]+=1
b=a-1
for i in b:
    e[i+1]+=1
c=a+1
for i in c:
    f[i+1]+=1
g=d+e+f
print(max(g))
