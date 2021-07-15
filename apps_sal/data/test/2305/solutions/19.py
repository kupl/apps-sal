import sys
sys.setrecursionlimit(10**6)
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

n = ni()
color = nl()
g = [list() for _ in range(n)]
for _ in range(n-1):
    a, b = nm()
    g[a-1].append(b-1)
    g[b-1].append(a-1)

size = [1]*n
par = [-1]*n
h = [list() for _ in range(n+1)]
idx = [0]*n
def dfs(v, p):
    h[color[v]].append(v)
    for x in g[v]:
        if x == p: continue
        par[x] = v
        size[v] += dfs(x, v)
        h[color[v]].append(v)
    h[color[v]].append(v)
    return size[v]
dfs(0, -1)
# print(size)
for v in range(n):
    if idx[v] < len(g[v]) and g[v][idx[v]] == par[v]:
        idx[v] += 1
acc = [0]*(n+10)
ans = [n*(n+1)//2]*(n+1)
for col in range(1, n+1):
    # print(h[col])
    acc[-1] = 0
    p = [-1]
    for v in h[col]:
        if p[-1] == v:
            p.pop()
            if idx[v] >= len(g[v]):
                acc[p[-1]] += size[v]
                continue
            q = size[g[v][idx[v]]] - acc[v]
            idx[v] += 1
            if idx[v] < len(g[v]) and g[v][idx[v]] == par[v]:
              idx[v] += 1
            ans[col] -= q*(q+1)//2
            acc[v] = 0
            # print(v, q)
            p.append(v)
        else:
            p.append(v)
    q = n - acc[-1]
    # print(-1, q)
    ans[col] -= q*(q+1)//2
print(*ans[1:], sep='\n')
