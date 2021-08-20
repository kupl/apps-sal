from functools import lru_cache
N = int(input())
K = int(input())


@lru_cache(None)
def f(n, k):
    if k < 0:
        return 0
    if n < 10:
        if k == 0:
            return 1
        elif k == 1:
            return n
        else:
            return 0
    (a, b) = divmod(n, 10)
    return f(a, k) + f(a, k - 1) * b + f(a - 1, k - 1) * (9 - b)


print(f(N, K))
