import sys
from heapq import heappop, heappush
N, M = list(map(int, sys.stdin.readline().split()))
A = [[] for _ in [0]*M]
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    if a > M:
        continue
    A[M-a].append(b)

ans = 0
q = []
for i, B in enumerate(A):
    for b in B:
        heappush(q, b)
        ans += b
    while len(q) > i+1:
        b = heappop(q)
        ans -= b
print(ans)

