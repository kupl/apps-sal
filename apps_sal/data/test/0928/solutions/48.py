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

    n, k = LI()
    a = [0] + LI()
    ac = list(itertools.accumulate(a))

    ans = 0
    now = 0

    for i in range(1, n + 1):
        for j in range(now, n + 1):
            if ac[now] - ac[i - 1] >= k:
                ans += n - now + 1
                break
            else:
                now += 1
        else:
            break

    print(ans)


main()
