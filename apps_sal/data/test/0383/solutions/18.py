MOD = 10 ** 9 + 7
(n, k, d) = [int(k) for k in input().split()]
ways1 = [0] * (n + 1)
ways1[0] = 1
ways1[1] = 1
for i in range(2, n + 1):
    for j in range(max(0, i - k), i):
        ways1[i] += ways1[j]
    ways1[i] %= MOD
ways2 = [0] * (n + 1)
ways2[0] = 1
ways2[1] = 1
if d == 1:
    ways2[0] = 0
    ways2[1] = 0
for i in range(2, n + 1):
    for j in range(max(0, i - (d - 1)), i):
        ways2[i] += ways2[j]
    ways2[i] %= MOD
print((ways1[n] - ways2[n]) % MOD)
