from collections import defaultdict
import functools
import bisect
import sys
import math
input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return list(map(int, input().split()))


def solve(case):
    [n, x] = inlt()
    aa = inlt()
    aa.sort()
    new_team = n - 1
    res = 0
    for i in range(n - 1, -1, -1):
        if aa[i] * (new_team - i + 1) >= x:
            res += 1
            new_team = i - 1
    return res


if len(sys.argv) > 1 and sys.argv[1].startswith('input'):
    f = open('./' + sys.argv[1], 'r')
    input = f.readline
T = inp()
for i in range(T):
    res = solve(i + 1)
    print(str(res))
