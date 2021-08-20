import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    return [w[0], w[1]]


def mod_inv(a, m=mod):
    x = extgcd(a, m)[0]
    return (m + x % m) % m


N2 = [1]
n = 1
for _ in range(N + 1):
    n = n * 2 % mod
    N2.append(n)
Weight = [[] for _ in range(N)]
checked = [False] * N


def dfs(p):
    checked[p] = True
    downs = 0
    for np in graph[p]:
        if not checked[np]:
            downscore = dfs(np)
            Weight[p].append(N - downscore)
            Weight[np].append(downscore)
            downs += N - downscore
    return N - (downs + 1)


dfs(0)
a = 0
for n in range(N):
    if len(Weight[n]) == 1:
        continue
    c = N2[N - 1] - 1
    for w in Weight[n]:
        c = (c - N2[w] + 1) % mod
    a = (a + c) % mod
ans = a * mod_inv(N2[N]) % mod
print(ans)
