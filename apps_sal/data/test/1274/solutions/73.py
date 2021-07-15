import sys
from collections import defaultdict
from heapq import heappop, heappush
N, M = list(map(int, sys.stdin.readline().split()))
A = defaultdict(list)
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    if a <= M:
    	A[M-a].append(b)

ans = 0
q = []
for i, B in sorted(A.items()):
    for b in B:
        heappush(q, b)
        ans += b
    while len(q) > i+1:
        b = heappop(q)
        ans -= b
print(ans)

