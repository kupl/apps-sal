def bpow(a, b):
    if b == 0 or a == 1:
        return 1
    if b % 2 != 0:
        return a * bpow(a, b - 1) % mod
    else:
        c = bpow(a, b / 2) % mod
        return c * c % mod


(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [0] + a + [n + 1]
a = sorted(a)
fa = list()
fa.append(1)
mod = 1000000007
for i in range(1, 2010):
    fa.append(fa[i - 1] * i)
    fa[i] %= mod
ans1 = 1
ans2 = 1
s = 0
for i in range(0, m + 1):
    ans1 *= fa[a[i + 1] - a[i] - 1]
    s += a[i + 1] - a[i] - 1
    ans1 %= mod
    if i > 0 and i < m and (a[i + 1] - a[i] > 1):
        ans2 *= pow(2, a[i + 1] - a[i] - 2, mod)
        ans2 %= mod
print(fa[s] * pow(ans1, mod - 2, mod) * ans2 % mod)
