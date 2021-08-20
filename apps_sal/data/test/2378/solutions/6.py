import sys
n = int(input())
mod = 10 ** 9 + 7
edge = [[] for i in range(n + 1)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
inv2 = [1] * (n + 1)
t = pow(pow(2, n, mod), mod - 2, mod)
for i in range(n, -1, -1):
    inv2[i] = t
    t *= 2
    t %= mod
sys.setrecursionlimit(10 ** 6)
dep = [-1 for i in range(n + 1)]
ans = [0]


def f(a):
    return inv2[n - a] * (1 - inv2[a]) % mod


def dfs(s, d):
    dep[s] = d
    tmp = inv2[1] - inv2[n]
    y = 0
    for i in edge[s]:
        if dep[i] == -1:
            x = dfs(i, d + 1)
            tmp -= f(x)
            y += x
    if y == 0:
        return 1
    tmp -= f(n - y - 1)
    ans[0] += tmp
    ans[0] %= mod
    return y + 1


dfs(1, 0)
print(ans[0])
