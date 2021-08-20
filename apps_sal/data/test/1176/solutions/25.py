import sys
import numpy as np
import math
n = int(input())
aList = list(map(int, input().split()))
numMinus = 0
for i in range(n):
    if aList[i] < 0:
        numMinus += 1
        aList[i] *= -1
aList.sort()
if numMinus % 2 == 0:
    print(sum(aList))
else:
    print(sum(aList) - 2 * aList[0])
