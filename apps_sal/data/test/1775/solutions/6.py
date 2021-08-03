from heapq import heappush, heappop
from sys import setrecursionlimit
from sys import stdin
from collections import defaultdict
setrecursionlimit(1000000007)
_data = iter(stdin.read().split('\n'))


def input():
    return next(_data)


n, m, k = [int(x) for x in input().split()]
a = tuple(tuple(-int(x) for x in input().split()) for i in range(n))
heaps = tuple([0] for _ in range(m))
removed = tuple(defaultdict(int) for _ in range(m))

rv = -1
rt = (0,) * m
t = [0] * m
p = 0
for i in range(n):
    ai = a[i]
    for j, v, heap in zip(range(m), ai, heaps):
        heappush(heap, v)
        t[j] = heap[0]
    while -sum(t) > k:
        ap = a[p]
        for j, v, heap, remd in zip(range(m), ap, heaps, removed):
            remd[v] += 1
            while heap[0] in remd:
                top = heappop(heap)
                if remd[top] == 1:
                    del remd[top]
                else:
                    remd[top] -= 1
            t[j] = heap[0]
        p += 1
    if rv < (i + 1) - p:
        rv = (i + 1) - p
        rt = tuple(t)
print(*map(lambda x: -x, rt))
