import sys
import math
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def main():
    S = SI()
    T = SI()
    D = defaultdict(str)
    for (s, t) in zip(S, T):
        if D[s] == '':
            D[s] = t
        if D[s] != t:
            print('No')
            return
    if len(set(D.keys())) != len(set(D.values())):
        print('No')
    else:
        print('Yes')


def __starting_point():
    main()


__starting_point()
