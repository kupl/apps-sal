import math
n = list(map(int, input().split()))
alist = list(map(int, input().split()))
sumpos = 0
maxNegOdd = -1000000000.0
maxPosODD = 1000000000.0
for i in alist:
    if i > 0:
        sumpos += i
        if i < maxPosODD and i % 2 != 0:
            maxPosODD = i
    elif i % 2 != 0 and maxNegOdd < i:
        maxNegOdd = i
if sumpos % 2 == 0:
    if maxPosODD > abs(maxNegOdd):
        sumpos += maxNegOdd
    else:
        sumpos -= maxPosODD
print(sumpos)
