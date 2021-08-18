import math
3
#coding: utf-8


N = int(input())
P = [[int(x) for x in input().split()] for _ in range(N)]


def calc(path):
    r = 0
    for i in range(len(path) - 1):
        p1 = P[path[i - 1]]
        p2 = P[path[i]]
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        r += math.sqrt(dx * dx + dy * dy)
    return r


ret = 0
numret = 0


def rec(path, rest):
    if not rest:
        nonlocal ret
        nonlocal numret
        ret += calc(path)
        numret += 1
        return
    for i in range(len(rest)):
        rec(path + [rest[i]], rest[:i] + rest[i + 1:])


rec([], [i for i in range(N)])
print((ret / numret))
