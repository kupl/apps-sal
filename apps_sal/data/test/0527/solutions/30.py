import sys
import math
from collections import deque
import bisect

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
    if set(S) | set(T) != set(S):
        print(-1)
        return
    s2i = {}

    for i, s in enumerate(S):
        if s in s2i:
            s2i[s].append(i)
        else:
            s2i[s] = [i]

    now = 0
    digit = -1
    for t in T:
        target = bisect.bisect_right(s2i[t], digit)
        if target == len(s2i[t]):
            digit = s2i[t][0]
            now += 1
        else:
            digit = s2i[t][target]

    print(now * len(S) + digit + 1)


def __starting_point():
    main()
__starting_point()
