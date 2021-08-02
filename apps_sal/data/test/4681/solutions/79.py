from functools import lru_cache


@lru_cache
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


N = int(input())
print((lucas(N)))
