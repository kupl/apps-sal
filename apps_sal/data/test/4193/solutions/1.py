from collections import deque
import itertools as it
from math import gcd
import math
from heapq import heappush, heappop, heapify
import time
import sys
read = sys.stdin.readline


def inp():
    return int(input())


def inpl():
    return list(map(int, input().split()))


start_time = time.perf_counter()
# ------------------------------

# bingo = [[0] * 3 for i in range(3)]
# bingo[0][0] = 1
# print(bingo)

bingo = []
for i in range(3):
    ls = inpl()
    bingo.append(ls)
N = inp()
for i in range(N):
    a = inp()
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == a:
                bingo[i][j] = -1

bl = False
for i in range(3):
    if bingo[i][0] == -1 and bingo[i][1] == -1 and bingo[i][2] == -1:
        bl = True
    if bingo[0][i] == -1 and bingo[1][i] == -1 and bingo[2][i] == -1:
        bl = True

if bingo[0][0] == -1 and bingo[1][1] == -1 and bingo[2][2] == -1:
    bl = True

if bingo[0][2] == -1 and bingo[1][1] == -1 and bingo[2][0] == -1:
    bl = True

print('Yes' if bl else 'No')


# -----------------------------
end_time = time.perf_counter()
print('time:', end_time - start_time, file=sys.stderr)
