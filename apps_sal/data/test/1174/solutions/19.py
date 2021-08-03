import sys
import math
import itertools
import collections
from collections import deque
import heapq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()


def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def main():

    N, M = NMI()
    A = NLI()

    A = list(map(lambda x: x * (-1), A))

    heapq.heapify(A)

    for m in range(M):
        highest = (heapq.heappop(A) * (-1))
        discounted = math.floor(highest / 2) * -1
        heapq.heappush(A, discounted)

    print(sum(A) * -1)
#


def __starting_point():
    main()


__starting_point()
