import sys
import math
d = []
for i in range(3):
    d.append([int(x) for x in sys.stdin.readline().split()])
a1 = sum(d[0]) - sum(d[1])
a2 = sum(d[1]) - sum(d[2])
for i in range(100000, 0, -1):
    d[0][0] = i
    d[1][1] = d[0][0] + a1
    d[2][2] = d[1][1] + a2
    if d[0][0] + d[1][1] + d[2][2] == sum(d[0]):
        break
for i in range(3):
    print(' '.join([str(x) for x in d[i]]))
