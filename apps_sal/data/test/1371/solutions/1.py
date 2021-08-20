def cmb(n, r, p):
    r = min(r, n - r)
    upper = 1
    for i in range(n, n - r, -1):
        upper = upper * i % p
    lower = 1
    for i in range(1, r + 1):
        lower = lower * i % p
    return upper * pow(lower, p - 2, p) % p


n = int(input())
mod = pow(10, 9) + 7
m = n // 3
ans = 0
for i in range(1, m + 1):
    x = n - 3 * i
    ans += cmb(x + i - 1, i - 1, mod)
    ans %= mod
print(ans)
