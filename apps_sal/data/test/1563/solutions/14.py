__autor__ = 'Esfandiar'
import sys
input=sys.stdin.readline
from collections import defaultdict
n,m = list(map(int,input().split()))
c = list(map(int,input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    u,v = list(map(int,input().split()))
    g[u-1].append(v-1)
    g[v-1].append(u-1)
color = defaultdict(list)
for u in range(n):
    color[c[u]].append(u)

M = -float('inf')
for k in list(color.keys()):
    seen = dict()
    res=0
    for v in color[k]:
        for u in g[v]:
            if c[u] != k and seen.get(c[u],-1)==-1:
                res+=1
                seen[c[u]]=1
        if res > M:
            M=res
            kk=k
        elif res == M:
            kk=min(kk,k)
print(kk)






'''
8 8
3 3 2 3 3 3 1 3
8 2
6 3
2 3
2 6
5 6
4 2
7 5
1 6
'''


