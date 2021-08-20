from functools import lru_cache
N = int(input())


@lru_cache(86)
def lucas(x):
    if x == 0:
        return 2
    if x == 1:
        return 1
    else:
        return lucas(x - 1) + lucas(x - 2)


print(lucas(N))
