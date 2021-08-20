from sys import stdin
from bisect import bisect_right as br
input = stdin.readline
(s, b) = map(int, input().split())
sp = list(map(int, input().split()))
bp = []
for i in range(b):
    bp.append(list(map(int, input().split())))
c = [0] * b
bp.sort()
for i in range(1, b):
    bp[i][1] += bp[i - 1][1]
an = [0] * s
for i in range(s):
    m = br(bp, [sp[i]])
    if m < b and bp[m][0] > sp[i]:
        m -= 1
    elif m == b:
        m -= 1
    if m >= 0:
        an[i] = bp[m][1]
    else:
        an[i] = 0
print(*an)
