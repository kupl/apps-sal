import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
C = [int(x) - 1 for x in input().split()]
E = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)


def dfs(u, p=-1):
    color = C[u]
    VC[color].append(u)
    s = 1
    for v in E[u]:
        if v == p:
            continue
        child[u] = 0
        ret = dfs(v, u)
        s += ret
        child[u] += ret
        ans[color] -= child[u] * (child[u] + 1) // 2
    VC[color].pop()
    if VC[color]:
        child[VC[color][-1]] -= s
    else:
        root_size[color] -= s
    return s


child = [0] * N
root_size = [N] * N
VC = [[] for _ in range(N)]
ans = [N * (N + 1) // 2] * N
dfs(0)
for i in range(N):
    print(ans[i] - root_size[i] * (root_size[i] + 1) // 2)
