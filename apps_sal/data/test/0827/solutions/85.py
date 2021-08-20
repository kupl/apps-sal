from sys import stdin, setrecursionlimit
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 1000000007


def input():
    return stdin.readline().strip()


def main():
    n = int(input())
    t = input()
    a = 10 ** 10
    ans = 0
    if n == 1:
        if t == '1':
            ans = a * 2
        elif t == '0':
            ans = a
    elif n == 2:
        if t in {'11', '10'}:
            ans = a
        elif t == '01':
            ans = a - 1
    elif n == 3:
        if t == '110':
            ans = a
        elif t in {'101', '011'}:
            ans = a - 1
    else:
        now = 0
        pre = t[:2]
        if pre == '11':
            now = 0
        elif pre == '10':
            now = 1
        elif pre == '01':
            now = 2
        else:
            print(0)
            return
        for char in t:
            flag = False
            if now in {0, 1}:
                if char != '1':
                    flag = True
            if now == 2:
                if char != '0':
                    flag = True
            now += 1
            if now == 3:
                now = 0
            if flag:
                print(0)
                return
        x = n if pre == '11' else n + 1 if pre == '10' else n + 2
        ans = a - ((x + 3 - 1) // 3 - 1)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
