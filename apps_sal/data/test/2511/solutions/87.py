import sys
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())
edges = [[] for _ in range(N)]
used = [False] * N
mod = 10**9 + 7
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


def f(n, c):
    sm = 1
    t = K - c
    for m in edges[n]:
        if not used[m]:
            used[m] = True
            if t <= 0:
                print(0)
                return
            sm = (sm * f(m, 2) * t) % mod
            t -= 1
    return sm


used[0] = True
print(K * f(0, 1) % mod)
