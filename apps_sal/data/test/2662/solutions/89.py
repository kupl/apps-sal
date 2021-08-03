import heapq
import bisect
N = int(input())
A = []

for i in range(N):
    a = int(input())
    A.append(a)
h = []
c = 0
for i in range(N - 1, -1, -1):
    p = bisect.bisect_right(h, A[i])
    if p == len(h):
        h.append(A[i])
        c += 1
    else:
        h[p] = A[i]
print(c)
