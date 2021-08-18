import io
import sys
import time
import random


r, c, n, k = list(map(int, input().split()))
data = [[0 for i in range(c)] for j in range(r)]

for i in range(n):
    x, y = list(map(int, input().split()))
    data[x - 1][y - 1] = 1

nviolists = [[0 for i in range(c)] for j in range(r)]

for r1 in range(r):
    count = 0
    for c1 in range(c):
        count += data[r1][c1]
        nviolists[r1][c1] = (nviolists[r1 - 1][c1] if r1 > 0 else 0) \
            + count

count = 0
for r1 in range(r):
    for r2 in range(r1, r):
        for c1 in range(c):
            for c2 in range(c1, c):

                vcount = nviolists[r2][c2] \
                    - (nviolists[r1 - 1][c2] if r1 > 0 else 0) \
                    - (nviolists[r2][c1 - 1] if c1 > 0 else 0) \
                    + (nviolists[r1 - 1][c1 - 1] if r1 * c1 > 0 else 0)
                if vcount >= k:
                    count += 1


print(count)
