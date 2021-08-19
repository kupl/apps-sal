import sys
from math import ceil
input = sys.stdin.readline
(n, t) = map(int, input().split())
choose = []
for i in range(1, n + 1):
    (a, b) = map(int, input().split())
    if a < t:
        a += ceil((t - a) / b) * b
    choose.append((a - t, i))
choose.sort()
print(choose[0][1])
