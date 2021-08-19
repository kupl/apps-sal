import math
import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
INF = float('inf')


def sol():
    N = int(input())
    engine = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for direct in range(0, 1000):
        direct = 2 * math.pi / 999 * direct
        (u, v) = (math.cos(direct), math.sin(direct))
        length = [0, 0]
        for (x, y) in engine:
            if u * x + v * y >= 0:
                length[0] += x
                length[1] += y
        ans = max(ans, length[0] ** 2 + length[1] ** 2)
    print(ans ** 0.5)


sol()
