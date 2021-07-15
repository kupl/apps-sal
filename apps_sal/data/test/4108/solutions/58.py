import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = SI()
    T = SI()
    D = defaultdict(str)
    for s, t in zip(S, T):
        if D[s] == "":
            D[s] = t
        if D[s] != t:
            print("No")
            return
    if len(set(D.keys())) != len(set(D.values())):
        print("No")
    else:
        print("Yes")


def __starting_point():
    main()
__starting_point()
