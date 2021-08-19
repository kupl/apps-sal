import sys
from heapq import heappop, heappush
from math import log2


# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, s.split())) for s in sys.stdin)


def bribe(n, a):
    if a[-1] < 0:
        return 0

    fr = a.index(-1)
    a[fr] = float('inf')
    h = int(log2(n))
    k = int(log2(fr + 1))
    total = a[-1]
    hq = []
    for r in range(h - 1, k, -1):
        [heappush(hq, a[i]) for i in range(2 ** r - 1, 2 ** (r + 1) - 1)]
        opponent = heappop(hq)
        total += opponent
    return total


n, = next(reader)
a = list(next(reader))
ans = bribe(n, a)
print(ans)

# inf.close()
