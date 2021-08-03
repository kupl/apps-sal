from collections import defaultdict


def prime_factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N = int(input())
mod = 10**9 + 7
primes = defaultdict(int)
for n in range(1, N + 1):
    for num, cnt in prime_factorization(n):
        primes[num] += cnt

ans = 1
for n, cnt in primes.items():
    if n == 1:
        continue
    ans *= cnt + 1
    ans %= mod
print(ans)
