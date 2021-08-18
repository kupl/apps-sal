from heapq import heapify, heappop, heappush
from collections import deque
N, M = list(map(int, input().split()))
A = [0] * N
B = [0] * N
C = [0] * N
for i in range(N):
    A[i], B[i] = list(map(int, input().split()))
    C[i] = [A[i], B[i]]
C.sort()
D = deque(C)
reward = 0

h = []
heapify(h)

for i in range(M - 1, -1, -1):
    while D:
        e = D.popleft()
        if e[0] == M - i:
            heappush(h, -1 * e[1])
        else:
            D.appendleft(e)
            break
    if h:
        reward += (-1) * heappop(h)

print(reward)
