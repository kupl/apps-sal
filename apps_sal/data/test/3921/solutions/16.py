import math

primes = []


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)


SieveOfEratosthenes(6000)
dp = [0 for i in range(max(primes) + 1)]

n = int(input())
arr = list(map(int, input().strip().split()))
try:
    for i in arr:
        p = []
        for j in primes:
            if j > i:
                break
            if i % j == 0:
                p.append(j)

        maxi = 0
        for j in p:
            maxi = max(dp[j] + 1, maxi)
        for j in p:
            dp[j] = maxi

    print(max(max(dp), 1))
except Exception as e:
    print(e)
