from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations
import sys
import bisect
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
YNeos = 'YNeos'
GYN = ['Yes', 'trumpet']
mo = 10 ** 9 + 7
imp = 'IMPOSSIBLE'
s = list(input())
di = defaultdict(int)
for i in range(len(s) - 1):
    di[int(s[i]), int(s[i + 1])] += 1
mp = [[[[0] * 10 for i in range(10)] for j in range(10)] for k in range(10)]
for h in range(10):
    for w in range(10):
        for x in range(10):
            for y in range(10):
                zm = 10 ** 3
                for nx in range(11):
                    for ny in range(11):
                        if nx + ny == 0:
                            continue
                        if (x * nx + y * ny - (w - h)) % 10 == 0:
                            zm = min(zm, nx + ny - 1)
                if zm < 30:
                    zz = zm
                else:
                    zz = -1
                mp[h][w][x][y] = zz
ans = [[0] * 10 for i in range(10)]
for x in range(10):
    for y in range(10):
        for i in list(di.items()):
            if mp[i[0][0]][i[0][1]][x][y] == -1:
                ans[x][y] = -1
                break
            ans[x][y] += mp[i[0][0]][i[0][1]][x][y] * i[1]
for j in range(10):
    print(*ans[j])
