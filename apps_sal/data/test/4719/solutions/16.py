import numpy as np
n = int(input())
argList = [input() for _ in range(n)]
keys = list('abcdefghijklmnopqrstuvwxyz')
nMat = []
for s in argList:
    nList = [0] * 26
    for (i, k) in enumerate(keys):
        nList[i] = s.count(k)
    nMat.append(nList)
nMat = np.array(nMat)
minLst = nMat.min(axis=0)
ret = ''
for (i, num) in enumerate(minLst):
    for j in range(num):
        ret += keys[i]
print(ret)
