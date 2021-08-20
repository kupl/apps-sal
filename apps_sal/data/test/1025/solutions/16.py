from fractions import gcd
import sys


def solve():
    n = int(input())
    if n < 3:
        print(0)
        return
    (xs, ys) = (list(), list())
    for i in range(n):
        (x, y) = map(int, input().split())
        xs.append(x)
        ys.append(y)
    mem = [0] * 2002
    for i in range(n):
        slopes = dict()
        (x, y) = (xs[i], ys[i])
        for o in range(n):
            if o != i:
                (xo, yo) = (xs[o], ys[o])
                (xdiff, ydiff) = (x - xo, y - yo)
                div = gcd(xdiff, ydiff)
                xdiff //= div
                ydiff //= div
                tup = (xdiff, ydiff)
                if tup in slopes:
                    slopes[tup] += 1
                else:
                    slopes[tup] = 2
        for val in slopes:
            mem[slopes[val]] += 1
    for i in range(2, len(mem)):
        mem[i] //= i
    res = fact(n, 3)
    for i in range(3, len(mem)):
        res -= mem[i] * fact(i, 3)
    print(res)


def fact(n, k):
    (large, small) = (max(k, n - k), min(k, n - k))
    res = 1
    for i in range(large + 1, n + 1):
        res *= i
    for i in range(2, small + 1):
        res //= i
    return res


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
