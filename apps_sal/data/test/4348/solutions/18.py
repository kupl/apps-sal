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
s = input()
d = dict()
for l in s:
    d[l] = d.get(l, 0) + 1
ordA = ord('a')
ordZ = ord('z')
trLeter = ''
count = 0
for i in range(ordA, ordZ + 1):
    l = chr(i)
    x = min(d.get(l, 0), k)
    if x == k:
        trLeter = l
        count = x
        break
    k -= x
ordTr = ord(trLeter)
result = ''
for l in s:
    ordL = ord(l)
    if ordL >= ordTr:
        if ordL == ordTr:
            count -= 1
        if ordL == ordTr and count >= 0:
            continue
        result += l
print(result)
