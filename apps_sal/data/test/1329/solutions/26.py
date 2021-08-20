N = int(input())
primes = set(range(2, N + 1))
for i in range(2, int(N ** 0.5 + 1)):
    primes.difference_update(range(i * 2, N + 1, i))
primes = list(primes)
primes.sort()
div = [0] * len(primes)
for i in range(2, N + 1):
    num = i
    for (j, prime) in enumerate(primes):
        cnt = 0
        if num < prime:
            break
        while num % prime == 0:
            cnt += 1
            num //= prime
        div[j] += cnt
(c74, c24, c14, c4, c2) = (0, 0, 0, 0, 0)
for i in div:
    if i >= 74:
        c74 += 1
    if i >= 24:
        c24 += 1
    if i >= 14:
        c14 += 1
    if i >= 4:
        c4 += 1
    if i >= 2:
        c2 += 1
ans = 0
ans += c74
ans += c24 * (c2 - 1)
ans += c14 * (c4 - 1)
ans += c4 * (c4 - 1) // 2 * (c2 - 2)
print(ans)
