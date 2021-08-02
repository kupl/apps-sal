from collections import defaultdict
import math

N = int(input())
D = defaultdict(int)


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def prime_cnt(p, n):
    cnt = 0
    temp = p
    while temp <= n:
        cnt += n // temp
        temp *= p
    return cnt


def conb(n, r):
    if n <= 0 or n < r:
        return 0
    elif r == 1:
        return n
    else:
        return n * (n - 1) // 2


for p in primes(N):
    D[p] += prime_cnt(p, N)

C = [0] * 5
L = [3, 5, 15, 25, 75]

for i in D.values():
    for j in range(5):
        if i >= L[j] - 1:
            C[j] += 1

ans = 0
ans += conb(C[4], 1)
ans += conb(C[3], 1) * conb(C[0] - 1, 1)
ans += conb(C[2], 1) * conb(C[1] - 1, 1)
ans += conb(C[1], 2) * conb(C[0] - 2, 1)

print(ans)
