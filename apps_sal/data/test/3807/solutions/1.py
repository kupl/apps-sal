from sys import *
setrecursionlimit(1000000)


def c(n):
    if n < 8:
        return (n, n)
    t1 = int(n ** (1 / 3) + 1e-11)
    t2 = t1 - 1
    v1 = c(n - t1 * t1 * t1)
    v1 = (v1[0] + 1, v1[1] + t1 * t1 * t1)
    v2 = c(t1 * t1 * t1 - 1 - t2 * t2 * t2)
    v2 = (v2[0] + 1, v2[1] + t2 * t2 * t2)
    if v2 > v1:
        v1 = v2
    return v1


print(' '.join(map(str, c(int(input())))))
