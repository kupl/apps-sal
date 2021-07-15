import heapq
from collections import defaultdict
x, y, z, K = list(map(int, input().split()))
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)
visited = defaultdict(bool)
Q = [(-(A[0]+B[0]+C[0]), 0, 0, 0)]

for _ in range(K):
    S, i, j, k = heapq.heappop(Q)
    print((-S))
    if i+1 < x and not visited[i+1, j, k]:
        heapq.heappush(Q, (-(A[i+1]+B[j]+C[k]), i+1, j, k))
        visited[i+1, j, k] = True

    if j+1 < y and not visited[i, j+1, k]:
        heapq.heappush(Q, (-(A[i]+B[j+1]+C[k]), i, j+1, k))
        visited[i, j+1, k] = True

    if k+1 < z and not visited[i, j, k+1]:
        heapq.heappush(Q, (-(A[i]+B[j]+C[k+1]), i, j, k+1))
        visited[i, j, k+1] = True

