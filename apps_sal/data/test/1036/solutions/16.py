from sys import stdin, setrecursionlimit
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
setrecursionlimit(10**8)

INF = float("inf")
MOD = 1000000007


def input():
    return stdin.readline().strip()


def main():

    dic = dict()

    def solve(l, r, i):
        if (i, r - l) in dic:
            return dic[(i, r - l)]
        if (r - l == 1):
            return s[i]
        mid = (l + r) // 2
        a = solve(l, mid, i)
        b = solve(mid, r, (i + mid - l) % n)
        res = ""
        st = {a, b}
        if st == set("RS"):
            res = "R"
        elif st == set("PR"):
            res = "P"
        elif st == set("SP"):
            res = "S"
        else:
            res = a
        dic[(i, r - l)] = res
        return res

    n, k = list(map(int, input().split()))
    s = input()
    ans = solve(0, pow(2, k), 0)
    print(ans)

    return


def __starting_point():
    main()


__starting_point()
