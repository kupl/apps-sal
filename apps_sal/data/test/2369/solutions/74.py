(n, k) = map(int, input().split())
a = sorted(list(map(int, input().split())))
p = 10 ** 9 + 7


def fact(n, p):
    a = [[] for _ in range(n + 1)]
    a[0] = 1
    for i in range(n):
        a[i + 1] = a[i] * (i + 1) % p
    return a


f = fact(n, p)
g = []
for i in range(n + 1):
    g.append(pow(f[i], -1, p))


def com(n, r):
    return f[n] * g[r] * g[n - r]


ans = 0
for i in range(n - k + 1):
    ans = ans + (a[-i - 1] - a[i]) * com(n - i - 1, k - 1)
print(ans % p)
