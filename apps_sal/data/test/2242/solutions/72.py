import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
def input(): return sys.stdin.readline().strip()


def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def combinations_count(n, r):
    if n == 1:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    S = SI()

    ls = []
    len_S = len(S)
    rem = 0

    for s in range(len_S - 1, -1, -1):
        rem = (rem + int(S[s]) * pow(10, len_S - s - 1, 2019)) % 2019
        ls.append(rem)

    import collections

    cls = collections.Counter(ls)
    clsv = list(cls.values())

    ans = 0

    for p in clsv:
        ans += combinations_count(p, 2)
    ans += cls[0]
    print(ans)


def __starting_point():
    main()


__starting_point()
