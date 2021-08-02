
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]


min_val, max_val = getints()


def get_key(pos, is_small, is_large, found):
    return ((pos * 2 + is_small) * 2 + is_large) * 2 + found


mod = 10**9 + 7
cache = [-1] * get_key(64, 1, 1, 1)


def solve(pos, is_small, is_large, found):
    if pos < 0:
        return 1
    key = get_key(pos, is_small, is_large, found)
    res = cache[key]
    if res >= 0:
        return res

    res = 0
    for x in [0, 1]:
        for y in [0, 1]:
            if x == 1 and y == 0: continue
            if not is_small and x == 0 and (min_val >> pos & 1) == 1:
                continue
            if not is_large and y == 1 and (max_val >> pos & 1) == 0:
                continue
            if not found and x != y:
                continue
            new_is_small = True if x > (min_val >> pos & 1) else is_small
            new_is_large = True if y < (max_val >> pos & 1) else is_large
            new_found = True if x == y and x == 1 else found
            res += solve(pos - 1, new_is_small, new_is_large, new_found)

    res = res % mod
    cache[key] = res
    return res


print(solve(63, False, False, False))
