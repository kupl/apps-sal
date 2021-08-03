from sys import *
setrecursionlimit(1000000)
# d={}


def c(n):
    #    t=d.get(n,(0,0))
    #    if t!=(0,0): return t
    if n < 8:
        return n, n
    t1 = int(n**(1 / 3) + 0.00000000001)
    t2 = t1 - 1
    v1 = c(n - t1 * t1 * t1)
    v1 = v1[0] + 1, v1[1] + t1 * t1 * t1
    v2 = c(t1 * t1 * t1 - 1 - t2 * t2 * t2)
    v2 = v2[0] + 1, v2[1] + t2 * t2 * t2
    if v2 > v1:
        v1 = v2
#    d[n]=v1
    return v1


print(' '.join(map(str, c(int(input())))))
