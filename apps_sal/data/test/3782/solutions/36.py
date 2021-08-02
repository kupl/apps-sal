import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)


def input():
    return sys.stdin.readline()[:-1]


mod = 10**9 + 7


def I(): return int(input())
def LI(): return list(map(int, input().split()))


def LIR(row, col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################


N, K, Q = LI()
A = LI()

# 最小値を決め打ちすると区間を分割できる

Aval = set(A)
ans = float('inf')
for a in Aval:
    now = []
    mins = []
    num = 0
    for i in range(N):
        if A[i] >= a:
            now.append(A[i])
        else:
            if len(now) >= K:
                now.sort()
                mins.extend(now[:len(now) - K + 1])
                num += len(now) - K + 1
            now = []
    if len(now) >= K:
        now.sort()
        mins.extend(now[:len(now) - K + 1])
        num += len(now) - K + 1
    if num >= Q:
        mins.sort()
        if mins[Q - 1] - a < ans:
            ans = mins[Q - 1] - a

print(ans)
