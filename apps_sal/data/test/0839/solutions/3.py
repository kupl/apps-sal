from itertools import *
a=[]
for i in range(5):
    a.append(list(map(int,input().split())))
ans=[]
m=0
for p in permutations(range(5)):
    t=0
    for i in range(4):
        for j in range(i,5,2):
            if j!=4:
                t+=a[p[j]][p[j+1]]+a[p[j+1]][p[j]]
    if t>=m:
        m=t
print(m)
