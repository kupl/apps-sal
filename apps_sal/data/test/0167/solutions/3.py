import math


def prefixIds(a, b):
    prefSubsId = [math.inf] * len(b)

    # print(a)
    # print(b)

    bId = 0
    aId = 0

    while aId < len(a):
        if bId == len(b):
            break

        if a[aId] == b[bId]:
            prefSubsId[bId] = aId + 1
            bId += 1
            aId += 1
        else:
            aId += 1

    return prefSubsId


a = input()
b = input()

# print(a)
# print(b)

n = len(b)

prefLens = prefixIds(a, b)
suffLens = prefixIds(a[::-1], b[::-1])[::-1]

# for i in range(n):
# 	if suffLens[i] != math.inf:
# 		suffLens[i] = len(a) - suffLens[i]

# print(*prefLens, sep='\t')
# print(*suffLens, sep='\t')

prefLen = 0
suffLen = 0

minCutLen = n
lBorder = -1
rBorder = n

while suffLen < n and suffLens[suffLen] == math.inf:
    suffLen += 1

curCutLen = suffLen
# print(curCutLen)
if curCutLen < minCutLen:
    minCutLen = curCutLen
    rBorder = suffLen

while prefLen < suffLen and prefLens[prefLen] != math.inf:
    while suffLen < n and prefLens[prefLen] + suffLens[suffLen] > len(a):
        # print(suffLen)
        suffLen += 1
    # print(prefLen)
    # print(suffLen)
    curCutLen = suffLen - prefLen - 1
    # print(curCutLen)
    if curCutLen < minCutLen:
        minCutLen = curCutLen
        lBorder = prefLen
        rBorder = suffLen
    prefLen += 1
    # print(prefLens[prefLen])
    # print(suffLens[suffLen])
# 	# print()

# print("pref, suff")
# print(prefLen)
# print(suffLen)

# print(minCutLen)
# print(n)
# print(lBorder)
# print(rBorder)

if minCutLen == n:
    print('-')
elif minCutLen == 0:
    print(b)
else:
    print(b[:lBorder + 1] + b[rBorder:])

# print(maxPrefLen)
# print(maxSuffLen)
