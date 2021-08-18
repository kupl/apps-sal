from collections import Counter
import bisect
from itertools import permutations
import sys
import math
def R(): return list(map(int, input().split()))
def I(): return int(input())
def S(): return str(input())


def L(): return list(R())


a, b = R()

s = S()
l = len(s)
step = []

x, y = 0, 0

d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

step.append((0, 0))

for i in range(l):
    dx, dy = d[s[i]]
    x += dx
    y += dy

    step.append((x, y))

tx, ty = step[l]

for j in range(l):
    xj, yj = step[j]

    if tx == 0 and ty == 0:
        if a == xj and b == yj:
            print('Yes')
            return

        else:
            continue

    if tx == 0 and (a != xj or (b - yj) % ty != 0 or ((b - yj) % ty == 0 and (b - yj) / ty < 0)):
        continue

    if ty == 0 and (b != yj or (a - xj) % tx != 0 or ((a - xj) % tx == 0 and (a - xj) / tx < 0)):
        continue

    if tx == 0 or ty == 0:
        print('Yes')
        return

    if (a - xj) % tx == 0 and (b - yj) % ty == 0 and (a - xj) / tx == (b - yj) / ty >= 0:
        print('Yes')
        return


print('No')
