from functools import lru_cache

n, a, b = map(int, input().split())
a -= 1
b -= 1

if n == 0:
    print(0)
    return


@lru_cache(maxsize=None)
def cnt(n):
    if n == 1:
        return 1
    return 2 * cnt(n >> 1) + 1


z = cnt(n)


@lru_cache(maxsize=None)
def query(n, l, r):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if r < cnt(n >> 1):
        return query(n >> 1, l, r)
    if l > cnt(n >> 1):
        return query(n >> 1, l - cnt(n >> 1) - 1, r - cnt(n >> 1) - 1)

    res = n & 1
    if l < cnt(n >> 1):
        res += query(n >> 1, l, cnt(n >> 1) - 1)
    if r > cnt(n >> 1):
        res += query(n >> 1, 0, r - cnt(n >> 1) - 1)

    #print("n={}, l={}, r={} => {}".format(n, l, r, res))
    return res


print(query(n, a, b))
