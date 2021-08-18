from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()

r1, c1 = mi()

r2, c2 = mi()

r1 = r1 - 1
c1 = c1 - 1
r2 = r2 - 1
c2 = c2 - 1


g = []

for i in range(n):
    g.append(li())


cc1 = set()


stack = [(r1, c1)]

while stack:
    r, c = stack.pop()
    cc1.add((r, c))
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if i == 0 or j == 0:
                    if r + i in range(0, n) and c + j in range(0, n):
                        if not (r + i, c + j) in cc1:
                            if g[r + i][c + j] == '0':
                                stack.append((r + i, c + j))


cc2 = set()


stack = [(r2, c2)]

while stack:
    r, c = stack.pop()
    cc2.add((r, c))
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if i == 0 or j == 0:
                    if r + i in range(0, n) and c + j in range(0, n):
                        if not (r + i, c + j) in cc2:
                            if g[r + i][c + j] == '0':

                                stack.append((r + i, c + j))


dist = 10 * n * n

for x, y in cc1:
    for x1, y1 in cc2:
        d = (x - x1)**2 + (y - y1)**2
        dist = min(d, dist)

print(dist)
