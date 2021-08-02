from heapq import heappop, heappush, heapify
from collections import deque

N, M = map(int, input().split())
A, B, C = [0] * N, [0] * N, [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
    C[i] = [A[i], B[i]]
C.sort()
C = deque(C)

a = []
heapify(a)
ans = 0

for i in range(M, -1, -1):
    while C:
        if C[0][0] <= M - i:
            heappush(a, (-1) * C[0][1])
            C.popleft()
        else:
            break
    if len(a) > 0:
        p = heappop(a)
        ans += (-1) * p

print(ans)
