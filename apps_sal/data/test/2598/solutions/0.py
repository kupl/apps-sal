from collections import deque
 
n, m = list(map(int, input().split()))
adj = [[] for i in range(n)]
for i in range(m):
    u, v, c = input().split()
    u, v = int(u)-1, int(v)-1
    adj[u].append((v, c))
    adj[v].append((u, c))
 
visited = S = T = None
 
def bfs(i, k):
    q = deque([(i, 0)])
    while q:
        u, p = q.pop()
 
        if visited[u] >= 0:
            if visited[u] == p: continue
            else: return False
 
        visited[u] = p
        if p: S.append(u)
        else: T.append(u)
 
        for v, c in adj[u]:
            nxt = p if c == k else p^1
            q.appendleft((v, nxt))
 
    return True
 
def solve(k):
    nonlocal visited, S, T
    visited = [-1]*n
    res = []
    for i in range(n):
        if visited[i] < 0:
            S, T = [], []
            if not bfs(i, k):
                return [0]*(n+1)
            else:
                res.extend(S if len(S) < len(T) else T)
    return res
 
res1 = solve("R")
res2 = solve("B")
 
if min(len(res1), len(res2)) > n:
    print(-1)
else:
    print(min(len(res1), len(res2)))
    print(" ".join([str(x+1) for x in res1 if len(res1) < len(res2) else res2]))

