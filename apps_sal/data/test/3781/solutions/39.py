# problem: let's play nim
# problem id: arc105 d

import sys
from collections import Counter


def input():
    return sys.stdin.readline()


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 != 0:
        print("Second")
    else:
        prt = dict(Counter(a))
        if any(v % 2 != 0 for v in list(prt.values())):
            print("First")
        else:
            print("Second")
    return


def main():
    t = int(input())
    for i in range(t):
        solve()
    return


def __starting_point():
    main()


__starting_point()
