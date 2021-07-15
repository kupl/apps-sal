from itertools import *
n,m=map(int,input().split())
M=m
a=[1]
for i in range(2,int(m**.5)+1):
    while m%i==0:
        m//=i
        a+=[i]
if m!=1:a+=[m]
ans=1
for i in range(len(a)):
    for b in combinations_with_replacement(set(a),i):
        c=1
        for j in b:c*=j
        if c>=n and M%c==0:ans=max(ans,M//c)
print(ans)
