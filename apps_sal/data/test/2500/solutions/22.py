from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n % 2 == 0:
        return (2 * f(n // 2 - 1) + f(n // 2)) % 1000000007
    else:
        return (2 * f(n // 2) + f(n // 2 - 1)) % 1000000007


n = int(input())
print(f(n))
