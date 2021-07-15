from functools import lru_cache

mod = 10 ** 9 + 7

@lru_cache(maxsize=None)
def f(n):
    if n <= 1:
        return n + 1
    return (f(n // 2) + f((n - 1) // 2) + f((n - 2) // 2)) % mod

N = int(input())
print(f(N))
