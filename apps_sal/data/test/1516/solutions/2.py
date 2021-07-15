mod = 998244353
n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    x = a[i]
    cur, pw = 0, 1
    while x:
        cur += 11 * (x % 10) * pw
        x = x // 10
        pw *= 100
    s += cur
    if s >= mod:
        s %= mod
print((s * n) % mod)
