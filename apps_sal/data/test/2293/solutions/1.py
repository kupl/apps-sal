import math
from sys import stdin, stdout


def input():
    return stdin.readline()[:-1]


m, n = list(map(int, input().split()))

days = []
for i in range(m):
    days.append(set(list(map(int, input().split()))[1:]))
possible = True
for i in range(m):
    for j in range(i):
        if not days[i].intersection(days[j]):
            possible = False
            break
    if not possible:
        break

if possible:
    print('possible')
else:
    print('impossible')
