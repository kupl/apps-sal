import functools
import sys
def input(): return sys.stdin.readline()


@functools.lru_cache(maxsize=10000)
def factor(n):
    res = []
    d = 2

    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1

    if n > 1:
        res.append(n)

    return set(res)


def Main(n):
    A = list(map(int, input().split()))[:n]
    dic = dict()

    for p in A:
        for d in factor(p):
            if d in dic.keys():
                dic[d] += 1
            else:
                dic[d] = 1

    if dic:
        print(max(dic.values()))
    else:
        print(1)


def __starting_point():
    n = int(input())
    Main(n)


__starting_point()
