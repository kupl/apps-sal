import sys
import heapq
mmx = 200000
ftree = [0] * (mmx + 1)


def uu(i, j, v):
    while i <= mmx:
        ftree[i] += v
        i += i & -i
    j += 1
    while j <= mmx:
        ftree[j] -= v
        j += j & -j


def qq(j):
    s = 0
    while j > 0:
        s += ftree[j]
        j -= j & -j
    return s


(n, k) = [int(i) for i in sys.stdin.readline().split()]
lns = sys.stdin.readlines()
bds = []
for j in range(n):
    t = [int(i) for i in lns[j].split()]
    t.append(j + 1)
    bds.append(t)
    uu(bds[-1][0], bds[-1][1], 1)
bds.sort()
bind = 0
heap = []
ans = []
for i in range(1, mmx + 1):
    while bind < n and bds[bind][0] == i:
        heapq.heappush(heap, (-1 * bds[bind][1], bds[bind][2]))
        bind += 1
    while qq(i) > k:
        (bd, bnd) = heapq.heappop(heap)
        ans.append(str(bnd))
        uu(i, -1 * bd, -1)
print(len(ans))
print(' '.join(ans))
