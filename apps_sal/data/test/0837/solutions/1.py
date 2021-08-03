from functools import lru_cache
import sys
sys.setrecursionlimit(100000)


@lru_cache()
def best(a):
    if a == 1:
        return x
    elif a > 0:
        if a == 2:
            return x + min(x, y)
        elif a % 2 == 0:

            return best(a // 2) + min(y, (a - a // 2) * x)
        else:
            return min(best(a - 1), best(a + 1)) + x


n, x, y = map(int, input().split())

print(best(n))
