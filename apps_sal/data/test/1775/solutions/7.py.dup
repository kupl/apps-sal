from heapq import heappush, heappop
from sys import setrecursionlimit
from sys import stdin
setrecursionlimit(1000000007)
_data = iter(stdin.read().split('\n'))


def input():
    return next(_data)


n, m, k = [int(x) for x in input().split()]
a = tuple(tuple(-int(x) for x in input().split()) for i in range(n))
heaps1 = tuple([0] for _ in range(m))
heaps2 = tuple([1] for _ in range(m))

rv = -1
rt = (0,) * m
t = [0] * m
p = 0
for i in range(n):
    ai = a[i]
    for j, v, heap1 in zip(range(m), ai, heaps1):
        heappush(heap1, v)
        t[j] = heap1[0]
    while -sum(t) > k:
        ap = a[p]
        for j, v, heap1, heap2 in zip(range(m), ap, heaps1, heaps2):
            heappush(heap2, v)
            while heap1[0] == heap2[0]:
                heappop(heap1)
                heappop(heap2)
            t[j] = heap1[0]
        p += 1
    if rv < (i + 1) - p:
        rv = (i + 1) - p
        rt = tuple(t)
print(*map(lambda x: -x, rt))
