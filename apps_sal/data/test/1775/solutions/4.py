from heapq import heappush, heappop
from sys import setrecursionlimit
from sys import stdin
from collections import defaultdict
setrecursionlimit(1000000007)
_data = iter(stdin.read().split('\n'))


def input():
    return next(_data)


(n, m, k) = [int(x) for x in input().split()]
a = tuple((tuple((-int(x) for x in input().split())) for i in range(n)))
heaps = tuple(([0] for _ in range(m)))
removed = tuple((defaultdict(int) for _ in range(m)))
rv = -1
rt = (0,) * m
p = 0
for i in range(n):
    ai = a[i]
    for j in range(m):
        heappush(heaps[j], ai[j])
    while -sum((heaps[j][0] for j in range(m))) > k:
        ap = a[p]
        for j in range(m):
            removed[j][ap[j]] += 1
            while heaps[j][0] in removed[j]:
                top = heappop(heaps[j])
                removed[j][top] -= 1
                if removed[j][top] == 0:
                    del removed[j][top]
                assert heaps[j]
        p += 1
    t = tuple((heaps[j][0] for j in range(m)))
    if rv < i + 1 - p:
        rv = i + 1 - p
        rt = t
print(*map(lambda x: -x, rt))
