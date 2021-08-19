mod = 10 ** 9 + 7
(n, a, b) = list(map(int, input().split()))
ans = pow(2, n, mod) - 1
comb1 = 1
for i in range(n - a + 1, n + 1):
    comb1 *= i
    comb1 %= mod
for i in range(1, a + 1):
    comb1 *= pow(i, mod - 2, mod)
    comb1 %= mod
comb2 = 1
for i in range(n - b + 1, n + 1):
    comb2 *= i
    comb2 %= mod
for i in range(1, b + 1):
    comb2 *= pow(i, mod - 2, mod)
    comb2 %= mod
ans -= comb1 + comb2
ans %= mod
print(ans)
