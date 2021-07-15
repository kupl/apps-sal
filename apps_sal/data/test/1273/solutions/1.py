import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N-1)]
es = [[] for _ in range(N)]
for i,(a,b) in enumerate(AB):
    a,b = a-1,b-1
    es[a].append((b,i))
    es[b].append((a,i))

ans = [None] * (N-1)

def dfs(v,p=-1,c=-1):
    nc = 1
    for to,e in es[v]:
        if to==p: continue
        if nc==c: nc += 1
        ans[e] = nc
        dfs(to,v,nc)
        nc += 1
dfs(0)

print(max(ans))
print(*ans, sep='\n')
