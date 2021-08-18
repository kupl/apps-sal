from functools import lru_cache

MOD = 10**9 + 7


@lru_cache(None)
def F(N):
    if N == 0:
        return 1, 1
    x, y = 0, 0
    x1, y1 = F(N // 2)
    x += x1
    y += x1
    x2, y2 = F((N - 1) // 2)
    x += x2
    y += y2
    if N > 1:
        x3, y3 = F((N - 2) // 2)
        x += y3
        y += y3

    return x % MOD, y % MOD


answer = F(int(input()))[0]

print(answer)
