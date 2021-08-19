from math import factorial


def count(n, r):
    if n == r:
        return 2
    else:
        return 1


(N, M) = map(int, input().split())
mod = 10 ** 9 + 7
print(factorial(N) % mod * (count(N, M) % mod) * (factorial(M) % mod) % mod if abs(N - M) < 2 else 0)
