n, k = map(int, input().split())
mod = 998244353
s = []
for _ in range(k):
    l, r = map(int, input().split())
    s += [(l, r)]

s.sort()
a = [0] * (n + 1)
a[1] = 1
for i in range(2, n + 1):
    a[i] = a[i - 1]
    for l, r in s:
        a[i] += a[max(0, i - l)] - a[max(0, i - r - 1)]
    a[i] %= mod
print((a[n] - a[n - 1]) % mod)
