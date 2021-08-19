from collections import *
import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def red(a, b, c):
    if a == 0 and b < 0:
        b, c = -b, -c
    if a < 0:
        a, b, c = -a, -b, -c
    g = gcd(a, gcd(abs(b), abs(c)))
    return a // g, b // g, c // g


def main():
    md = 998244353
    n = int(input())
    xy = LLI(n)
    cnt_online = {}
    # 各２点を結ぶ直線をax+by+c=0の(a,b,c)で表し
    # 各直線上にいくつの点があるかカウントする
    for i in range(n):
        x0, y0 = xy[i]
        counted = set()
        for j in range(i):
            x1, y1 = xy[j]
            a = y0 - y1
            b = x1 - x0
            c = -a * x0 - b * y0
            a, b, c = red(a, b, c)
            if (a, b, c) in counted:
                continue
            counted.add((a, b, c))
            cnt_online.setdefault((a, b, c), 1)
            cnt_online[(a, b, c)] += 1
    # print(cnt_online)
    # 各直線上で、2点以上で多角形ができない点の選び方を数える
    sum_online = 0
    for plot_n in cnt_online.values():
        sum_online += pow(2, plot_n, md) - 1 - plot_n
        sum_online %= md
    # すべての2点以上の選び方から、多角形ができないものを引く
    ans = pow(2, n, md) - 1 - n - sum_online
    print(ans % md)


main()
