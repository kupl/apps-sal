import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


pm = [-1, 1]

n, m = ma()
xyz = []
for i in range(n):
    xyz.append(lma())


def f(p0, p1, p2):
    xyz.sort(key=lambda x: p0 * x[0] + p1 * x[1] + p2 * x[2], reverse=True)
    ret = 0
    for i in range(m):
        t = xyz[i]
        ret += p0 * t[0] + p1 * t[1] + p2 * t[2]
    return ret


tmp = -10**15
for i in range(2**3):
    p = [1, 1, 1]
    for j in range(3):
        p[j] = pm[(i >> j) & 1]
    # print(p)
    # print(f(*p))
    tmp = max(tmp, f(*p))
print(tmp)
