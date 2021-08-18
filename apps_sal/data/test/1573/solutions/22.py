
import math

s = input().split()
n, d = int(s[0]), int(s[1])
ms = []
for _ in range(n):
    st = input().split()
    if int(st[1]):
        ms.append((int(st[0]), (int(st[1]))))

ms = sorted(ms, key=lambda i: i[0])
m, s = [], []
for i in ms:
    m.append(i[0])
    s.append(i[1])

ssums = [0]
for i in s:
    ssums.append(ssums[-1] + i)
maxsSum = 0
iOverMaxEl = 1
for iMinEl in range(len(m)):
    if iOverMaxEl <= iMinEl:
        iOverMaxEl = iMinEl + 1
    while iOverMaxEl < len(s) and m[iOverMaxEl] - m[iMinEl] < d:
        iOverMaxEl += 1
    sSum = ssums[iOverMaxEl] - ssums[iMinEl]
    if sSum > maxsSum:
        maxsSum = sSum

print(maxsSum)
