import bisect
import collections
import copy
import itertools
import math
import string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():

    n = I()
    a = [0] + LI()
    ans = [0 for _ in range(n + 1)]

    for i in range(n, 0, -1):
        cnt = 0
        for j in range(i, n + 1, i):
            cnt += ans[j]
        if cnt % 2 != a[i]:
            ans[i] = 1

    ans_lst = []
    for i in range(1, n + 1):
        if ans[i] == 1:
            ans_lst.append(i)

    print((len(ans_lst)))
    print((*ans_lst))


main()
