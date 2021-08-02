import heapq

N, M = map(int, input().split())
A = list(map(lambda x: int(x) * (-1), input().split()))
heapq.heapify(A)

for _ in range(M):
    tmp_min = heapq.heappop(A)
    heapq.heappush(A, (-1) * (-tmp_min // 2))

print(-sum(A))
