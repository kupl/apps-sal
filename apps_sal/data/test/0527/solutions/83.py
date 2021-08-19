import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


def main():
    s = S()
    n = len(s)
    t = S()
    n2 = len(t)

    d = {}
    for i, x in enumerate(s):
        if x in d:
            y = d[x]
            y.append(i)
            d[x] = y
        else:
            d[x] = [i]

    # print(d)
    i = 0
    j = 0
    ans = 1
    while j < n2:
        check = t[j]
        if check not in d:
            return -1
        l = d[check]
        if i < l[0]:
            ans += l[0] - i + 1
            i = l[0] + 1
            j += 1
        elif l[-1] < i:
            ans += n - (i + 1) + l[0] + 2
            i = l[0] + 1
            j += 1
        else:
            if i == l[0]:
                ans += 1
                i += 1
                j += 1
            elif i == l[-1]:
                ans += 1
                i += 1
                j += 1
            else:
                left = 0
                right = len(l)
                while right - left > 1:
                    m = (right + left) // 2
                    if l[m] >= i:
                        right = m
                    else:
                        left = m
                    # print(right,left,m,i)
                ans += l[right] - i + 1
                i = l[right] + 1
                j += 1

        # print(i,ans)

        i %= n

    return ans - 1


# main()
print((main()))
