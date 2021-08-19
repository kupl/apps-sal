(n, k) = map(int, input().split())
mod = pow(10, 9) + 7
(c1, c2) = (1, 1)
(n1, n2) = (n, n - 1)
ans = 1
for r in range(1, min(k + 1, n)):
    c1 = c1 * n1 * pow(r, mod - 2, mod) % mod
    c2 = c2 * n2 * pow(r, mod - 2, mod) % mod
    n1 -= 1
    n2 -= 1
    ans += c1 * c2 % mod
    ans %= mod
print(ans)
