from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
sys.setrecursionlimit(10 ** 6)


def SI():
    return input().split()


def MI():
    return list(map(int, input().split()))


def I():
    return int(input())


def LI():
    return [int(i) for i in input().split()]


YN = ['Yes', 'No']
mo = 10 ** 9 + 7
a = []
(n, m) = MI()
for i in range(n):
    h = LI()
    a.append(h)
b = [[0] * m for i in range(n)]
ans = []
for r in range(n - 1):
    for c in range(m - 1):
        if a[r][c] + a[r + 1][c] + a[r][c + 1] + a[r + 1][c + 1] == 4:
            ans += [(r + 1, c + 1)]
            b[r][c] = 1
            b[r][c + 1] = 1
            b[r + 1][c] = 1
            b[r + 1][c + 1] = 1
if a == b:
    print(len(ans))
    for j in ans:
        print(*j)
else:
    print(-1)
