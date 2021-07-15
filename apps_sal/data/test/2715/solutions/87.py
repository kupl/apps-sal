import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    k = ni()
    l = 50
    ans = [l - 1 for _ in range(l)]

    for i in range(l):
        ans[i] += k // l
        
        tgt = k % l
        if i < tgt:
            ans[i] += l
            ans[i] -= tgt - 1
        else:
            ans[i] -= tgt

    print(l)
    print(*ans, sep=" ")


def __starting_point():
    main()

__starting_point()
