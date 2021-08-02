import sys
sys.setrecursionlimit(1000000000)
n, m = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
G = [[] for _ in range(n)]
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    G[c].append(d)
    G[d].append(c)
seen = [False] * n


def dfs(now):
    seen[now] = True
    sa = A[now]
    sb = B[now]
    for nxt in G[now]:
        if seen[nxt]: continue
        seen[nxt] = True
        a, b = dfs(nxt)
        sa += a
        sb += b
    return (sa, sb)


for i in range(n):
    if seen[i]: continue
    sa, sb = dfs(i)
    if sa != sb:
        print("No")
        return
print("Yes")
