n = int(input())
if n == 1:
    print(0)
    return
primes = [True] * (n + 1)
primes[0] = False
primes[1] = False
for i in range(2, n + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False
primes = [i for i, j in enumerate(primes) if j]
factors = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
for i in primes:
    tmp = 0
    j = i
    while j <= n:
        tmp += n // j
        j *= i
    for k in factors:
        if tmp >= k:
            factors[k] += 1
ans = factors[4] * (factors[4] - 1) * (factors[2] - 2) // 2
ans += factors[14] * (factors[4] - 1)
ans += factors[24] * (factors[2] - 1)
ans += factors[74]
print(ans)
