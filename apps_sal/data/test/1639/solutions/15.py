__author__ = 'pxy'
i=int(input())
g=[int(j) for j in input().split()]
k=1
maxx=0
for j in range(i-1):
    if g[j]<=g[j+1]:
        k+=1
    else:
        if(k>maxx):
            maxx=k
        k=1
print(max(k,maxx))
