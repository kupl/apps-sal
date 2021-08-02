from functools import reduce, lru_cache

INF = float("inf")

N, a, b, *A = map(int, open(0).read().split())
c = reduce(lambda a, b: a ^ b, A, 0)


@lru_cache(None)
def solve(a, b, c):
    if (a % 2) ^ (b % 2) != (c % 2):
        return INF
    if c == 0:
        return INF if a < b else (a - b) // 2

    return min(
        2 * solve(a // 2, b // 2, c // 2),
        1 + 2 * solve((a - 1) // 2, (b + 1) // 2, c // 2)
    )


print(-1 if (res := solve(a, b, c)) >= a else res)
