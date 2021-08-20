import math
from collections import defaultdict


def getInputList():
    return list(input().split())


def getInputIntList():
    return list(map(int, input().split()))


n = input()
arr = getInputIntList()
myset = defaultdict(lambda: 0)
for i in arr:
    myset[i] += 1
nset = set([])
for i in arr:
    cb = '1' + '0' * (len(bin(i)) - 3)
    if bin(i) == '0b' + cb:
        if myset[i] > 1:
            nset.add(i)
    elif int(cb + '0', 2) - i in myset:
        nset.add(i)
        nset.add(int(cb + '0', 2) - i)
count = 0
for i in arr:
    if i not in nset:
        count += 1
print(count)
