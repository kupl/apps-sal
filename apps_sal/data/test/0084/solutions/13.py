from math import *
import sys
#sys.stdin = open('in.txt')

n = int(input())


def closest9(n):
    s = '9' * (len(str(n + 1)) - 1)
    return 0 if len(s) == 0 else int(s)


def solve(n):
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n == 4:
        return 6
    s = n + n - 1
    c = closest9(s)
    if c * 10 + 9 == s:
        return 1
    p = c
    res = 0
    for i in range(10):
        if p <= n + 1:
            res += p // 2
        elif p > s:
            break
        else:
            res += 1 + (s - p) // 2
        #print(p, v)
        p += c + 1
    return res


print(solve(n))
