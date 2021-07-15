import sys
input = sys.stdin.readline
from math import sqrt


def Eratosthenes(n):
    """n(>=6)未満の素数列挙 """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(sqrt(n)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    # return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]
    # x が素数か判定したいとき
    return {2, 3}.union({3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]})


sieve = Eratosthenes(10 ** 5 + 1)
ans = [0] * (10 ** 5 + 1)
for i in range(3, 10 ** 5, 2):
    if i in sieve and (i + 1) // 2 in sieve:
        ans[i] += 1
for i in range(3, 10 ** 5):
    ans[i + 1] += ans[i]
q = int(input())
for i in range(q):
    l, r = list(map(int, input().split()))
    print((ans[r] - ans[l - 1]))

