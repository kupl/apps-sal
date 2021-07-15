import sys, math, re
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    S = input()
    l = [0]
    for i in range(N):
        if S[i] == '(':
            l.append(l[-1]+1)
        else:
            l.append(l[-1]-1)

    m = min(l)

    if m < 0:
        l = list(map(lambda x: x-m, l))

    print('('*l[0] + S + ')'*l[-1])

def __starting_point():
    main()
__starting_point()
