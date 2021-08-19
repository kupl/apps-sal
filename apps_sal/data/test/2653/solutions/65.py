import sys
sys.setrecursionlimit(10 ** 9)
(N, Q) = map(int, input().split())
T = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    T[a].append(b)
    T[b].append(a)
V = [0] * N
for _ in range(Q):
    (p, x) = map(int, input().split())
    p -= 1
    V[p] += x


def dfs(now, prev=-1):
    for next in T[now]:
        if next == prev:
            continue
        V[next] += V[now]
        dfs(next, now)


dfs(0)
print(*V)
