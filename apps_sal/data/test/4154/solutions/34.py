import numpy as np


def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n, m = INTM()
    ls = []
    rs = []
    for i in range(m):
        l, r = INTM()
        ls.append(l)
        rs.append(r)

    ans = min(rs) - max(ls) + 1
    if ans <= 0:
        ans = 0
    print(ans)


def __starting_point():
    do()


__starting_point()
