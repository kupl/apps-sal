from functools import lru_cache


def mod(x):
    return x % (10 ** 9 + 7)


@lru_cache(maxsize=None)
def dp(i, j, k):
    if i == 0:
        if k == 0 and j == 0:
            return 1
        else:
            return 0
    elif k < 0 or j < 0 or i < j:
        return 0
    else:
        return mod((2 * j + 1) * dp(i - 1, j, k - 2 * j) + (j + 1) * (j + 1) * dp(i - 1, j + 1, k - 2 * j) + dp(i - 1, j - 1, k - 2 * j))


(n, k) = list(map(int, input().split()))
print(dp(n, 0, k))
