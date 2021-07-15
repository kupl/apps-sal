n,m = map(int,input().split())
g = [set() for i in range(n)]
from sys import stdin
for i in range(m):
    a,b = map(int,stdin.readline().split())
    g[a-1].add(b-1)
c = [0]*n
for i in range(n):
    c[i]=i
for i in range(n):
    j=i
    while j>0 and c[j] in g[c[j-1]]:
        c[j],c[j-1]=c[j-1],c[j]
        j-=1
for i in c:
    print(i+1,end=' ')
