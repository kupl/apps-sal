import sys
sys.setrecursionlimit(10 ** 9)
N, Q = map(int, input().split())

AB_TREE = [[] for i in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB_TREE[b].append(a)
    AB_TREE[a].append(b)

ans = [0] * (N + 1)

for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x


def dfs(v, p):
    for to in AB_TREE[v]:
        if to == p: continue
        ans[to] += ans[v]
        dfs(to, v)


dfs(0, -1)
for i in range(N):
    print(ans[i],end=' ')

