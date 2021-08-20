from bisect import bisect
import heapq
N = int(input())
A = [int(input()) for _ in range(N)]
q = []
A.reverse()
for i in range(N):
    ii = bisect(q, A[i])
    if ii == len(q):
        heapq.heappush(q, A[i])
    else:
        q[ii] = A[i]
print(len(q))
