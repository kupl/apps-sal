from collections import Counter, defaultdict
N = int(input())


def primeFactorization(N):
    primes = Counter()
    R = int(N ** 0.5) + 1
    for num in range(2, R):
        while N % num == 0:
            N //= num
            primes[num] += 1
    if N > 1:
        primes[N] = 1
    return primes


primes = Counter()
for i in range(1, N + 1):
    primes += primeFactorization(i)
cnt = defaultdict(int)
for c in list(primes.values()):
    c += 1
    for d in (3, 5, 15, 25, 75):
        if c >= d:
            cnt[d] += 1
ans = 0
ans += cnt[5] * (cnt[5] - 1) * (cnt[3] - 2) // 2
ans += cnt[25] * (cnt[3] - 1)
ans += cnt[15] * (cnt[5] - 1)
ans += cnt[75]
print(ans)
