import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
gift = list(map(int, (sys.stdin.readline().split())))

maxi = -1
maxval = -1

for i, x in enumerate(gift):
    if x >= 0:
        x = -1 * x - 1
        gift[i] = x
    if abs(x) > maxval:
        maxval = abs(x)
        maxi = i

if (n % 2) == 1:
    gift[maxi] = -1 * gift[maxi] - 1

print(' '.join([str(x) for x in gift]))
