n, k = map(int, input().split())

MOD = 1000003

K = k - 1

max_deg = 0

while K > 0:
    max_deg += K // 2
    K //= 2

den_deg = n * (k-1) - max_deg

kk = 1
for i in range(n):
    kk *= 2
    if kk >= k: break
else:
    print(1, 1)
    return

numerator = 1
two_p_n = pow(2, n, MOD)
for i in range(1, min(k, MOD + 1)):
    numerator *= (two_p_n - i + MOD) % MOD
    if numerator == 0: break
    numerator %= MOD

rev = (MOD + 1) // 2
numerator *= pow(rev, max_deg, MOD)
numerator %= MOD

denumerator = pow(2, den_deg, MOD)
numerator = (denumerator + MOD - numerator) % MOD

print(numerator, denumerator)
