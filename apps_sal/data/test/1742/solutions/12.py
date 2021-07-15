import sys
import heapq
import math
from enum import Enum

lines = sys.stdin.read().splitlines()
n, m = list(map(int, lines[0].split(' ')))
positionToNumber = [int(x)-1 for x in lines[1].split(' ')]

numberToPosition = [0]*n
for i in range(0, len(positionToNumber)):
    numberToPosition[positionToNumber[i]] = i

# print('numberToOrder: ' + str(numberToOrder))
letsInFront = []
for i in range(0, n):
    letsInFront.append(set())
for i in range(0, m):
    a, b = list(map(int, lines[i+2].split(' ')))
    # a lets b in front
    indexA = a-1
    indexB = b-1
    letsInFront[numberToPosition[indexA]].add(numberToPosition[indexB])

# for i in range(0, n):
#     letsInFront[i].sort()
# print(bitmaps)
count = 0
let = set()
let.add(n-1)
# print(letsInFront)
for i in reversed(list(range(0, n-1))):
    found = True
    if len(let) > len(letsInFront[i]):
        found = False
    else:
        for j in let:
            if j not in letsInFront[i]:
                found = False
                break
    if not found:
        let.add(i)
    else:
        count += 1
print(count)

