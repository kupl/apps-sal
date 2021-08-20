from heapq import *
from collections import *
from bisect import *
from itertools import permutations
import sys
sys.setrecursionlimit(10 ** 6)


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def SI():
    return sys.stdin.readline()[:-1]


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def int1(x):
    return int(x) - 1


def MI1():
    return map(int1, sys.stdin.readline().split())


def LI1():
    return list(map(int1, sys.stdin.readline().split()))


def p2D(x):
    return print(*x, sep='\n')


dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def main():
    (m, k) = MI()
    if (m, k) == (1, 1) or k >= 2 ** m:
        ans = [-1]
    elif k == 0:
        ans = list(range(1 << m))
        ans += ans[::-1]
    else:
        ans = []
        for i in range(1 << m):
            if i == k:
                continue
            ans.append(i)
        rev = ans[::-1]
        ans.append(k)
        ans += rev
        ans.append(k)
    print(*ans)


main()
