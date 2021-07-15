import sys
sys.setrecursionlimit(10**6)

MOD = 10**9+7

N,K = map(int,input().split())
edge = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

    
visit = [0]*N

def dfs(vs, pat, count):
    
    for ve in edge[vs]:
        if visit[ve]:continue
        
        visit[ve] = 1
        pat = pat*(K-count) % MOD
        count += 1
        pat = dfs(ve, pat, 2)
    
    return pat

visit[0] = 1

ans = dfs(0,K,1)
print(ans)
