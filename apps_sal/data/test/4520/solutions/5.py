from math import *
(n, k) = map(int, input().split())
num = [[] for i in range(300)]
segment = [0]
for i in range(1, n + 1):
    (l, r) = map(int, input().split())
    num[l].append(i)
    num[r + 1].append(-i)
    segment.append((l, r + 1, r - l))
rep = 0
curSegment = []
rem = []
for i in range(300):
    for a in num[i]:
        if a >= 0:
            curSegment.append(a)
        elif -a in curSegment:
            curSegment.remove(-a)
    while len(curSegment) > k:
        rep += 1
        plusAdroite = 0
        aVirer = 0
        for j in curSegment:
            if segment[j][1] >= plusAdroite:
                plusAdroite = segment[j][1]
                aVirer = j
        curSegment.remove(aVirer)
        rem.append(aVirer)
print(rep)
print(*sorted(rem))
