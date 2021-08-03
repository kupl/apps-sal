import math
import random
import time
import heapq


def getIntList():
    return list(map(int, input().split()))


def getTransIntList(n):
    first = getIntList()
    m = len(first)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        result[i][0] = first[i]
    for j in range(1, n):
        curr = getIntList()
        for i in range(m):
            result[i][j] = curr[i]
    return result


n, k = getIntList()
a = getIntList()
result = 0
for x in a:
    if x > k:
        break
    result += 1
if result < n:
    for x in a[::-1]:
        if x > k:
            break
        result += 1
print(result)
