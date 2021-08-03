def g(r, c):
    return (fact[r + c + 2] * fact_inv[r + 1] * fact_inv[c + 1] - 1) % mod


r1, c1, r2, c2 = list(map(int, input().split()))

mod = 10 ** 9 + 7
MAX = 10 ** 6

fact = [1] * (2 * MAX + 10)
for i in range(1, 2 * MAX + 10):
    fact[i] = (fact[i - 1] * i) % mod

inv = [1] * (MAX + 10)
for i in range(2, MAX + 10):
    inv[i] = inv[mod % i] * (mod - mod // i) % mod

fact_inv = [1] * (MAX + 10)
for i in range(1, MAX + 10):
    fact_inv[i] = fact_inv[i - 1] * inv[i] % mod

ans = g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)
ans %= mod
print(ans)
