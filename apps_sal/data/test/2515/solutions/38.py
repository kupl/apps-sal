from math import sqrt
import sys
input = sys.stdin.readline


def Eratosthenes(n):
    """n(>=6)未満の素数列挙 """
    (n, correction) = (n - n % 6 + 6, 2 - (n % 6 > 1))
    sieve = [True] * (n // 3)
    for i in range(1, int(sqrt(n)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    s = [False] * n
    for i in range(1, n // 3 - correction):
        if sieve[i]:
            s[3 * i + 1 | 1] = True
    s[2] = True
    s[3] = True
    return s


sieve = Eratosthenes(10 ** 5 + 1)
ans = [0] * (10 ** 5 + 1)
for i in range(3, 10 ** 5, 2):
    if sieve[i] and sieve[(i + 1) // 2]:
        ans[i] += 1
for i in range(3, 10 ** 5):
    ans[i + 1] += ans[i]
q = int(input())
for i in range(q):
    (l, r) = list(map(int, input().split()))
    print(ans[r] - ans[l - 1])
