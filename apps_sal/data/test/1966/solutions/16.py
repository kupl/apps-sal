
import sys

n = int(sys.stdin.readline().strip())
blks = []
for i in range(4):
    blks.append([])
    for j in range(n):
        blks[-1].append(sys.stdin.readline().strip())
    if i != 3:
        sys.stdin.readline()


def to_BW(blk):
    n = len(blk)
    BW = [0, 0]
    for i in range(n):
        for j in range(n):
            BW[(i + j + int(blk[i][j])) % 2] += 1
    return BW


BWs = [to_BW(blk) for blk in blks]

res = 4 * n**2

for i in range(4):
    for j in range(i):
        kl = list(set(range(4)) - {i, j})
        res = min(res, BWs[i][0] + BWs[j][0] + BWs[kl[0]][1] + BWs[kl[1]][1])

print(res)
