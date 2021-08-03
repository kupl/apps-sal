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


def main():

    N, K = NMI()
    A = NLI()

    left = 0
    right = 0
    shakutori = 0
    ans = 0

    for left in range(N):

        while shakutori < K and right < N:
            shakutori += A[right]
            right += 1

        if shakutori >= K:
            ans += N - right + 1
            shakutori -= A[left]
        else:
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
