import sys
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
p2 = [1] * (3 * 10**5)
for n in range(3 * 10**5 - 1):
    p2[n + 1] = p2[n] * 2 % mod

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
g = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = AB[i]
    g[a].append(b)
    g[b].append(a)

l1 = [0] * (N + 1)
l2 = [[] for _ in range(N + 1)]


def rec(p, c):
    res = 0
    for a in g[c]:
        if a == p:
            continue
        n = rec(c, a)
        l2[c].append(n + 1)
        res += n + 1
    l1[c] = res
    return res


n = rec(0, 1)
for i in range(1, N + 1):
    l2[i].append(N - 1 - l1[i])

ans = 0
for i in range(1, N + 1):
    ans += p2[N - 1] - 1
    ans %= mod
    for j in l2[i]:
        ans -= p2[j] - 1
        ans %= mod
ans *= pow(p2[N], mod - 2, mod)
ans %= mod
print(ans)
