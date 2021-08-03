fact = [1 for _ in range(1000000)]
inv = [1 for _ in range(1000000)]
fact_inv = [1 for _ in range(1000000)]

P = 10**9 + 7
for i in range(2, 1000000):
    fact[i] = (fact[i - 1] * i) % P
    inv[i] = P - (inv[P % i] * (P // i)) % P
    fact_inv[i] = (fact_inv[i - 1] * inv[i]) % P

X, Y = map(int, input().split())
res = 0
if (X + Y) % 3 == 0:
    a = (-X + 2 * Y) // 3
    b = (2 * X - Y) // 3
    if a >= 0 and b >= 0:
        res = fact[a + b] * ((fact_inv[a] * fact_inv[b]) % P) % P
print(res)
