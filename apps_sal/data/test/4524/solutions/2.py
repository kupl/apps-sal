mod = 998244353
(n, m) = map(int, input().split())
a = [0] * max(0, m - n) + list((int(ch) for ch in input()))
b = [0] * max(0, n - m) + list((int(ch) for ch in input()))
pow2 = 1
for i in range(len(a) - 2, -1, -1):
    pow2 = (pow2 << 1) % mod
    a[i] = (pow2 * a[i] + a[i + 1]) % mod
ans = 0
for i in range(len(b)):
    if b[i]:
        ans = (ans + a[i]) % mod
print(ans)
