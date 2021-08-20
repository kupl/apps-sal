from functools import lru_cache
MOD = 10 ** 9 + 7
(x, y) = map(int, input().split())
summ = x + y


@lru_cache(maxsize=None)
def inv(n):
    return pow(n, -1, MOD)


if summ % 3 == 0 and summ // 3 <= x and (summ // 3 <= y):
    mn = min(x, y)
    n = mn - summ // 3
    a = summ // 3
    b = 1
    ans = 1
    for i in range(n):
        ans *= a
        ans *= inv(b)
        ans %= MOD
        a -= 1
        b += 1
    print(ans)
else:
    print(0)
