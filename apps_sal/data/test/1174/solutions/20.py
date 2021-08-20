import heapq
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
ls = []
for item in A:
    heapq.heappush(ls, -item)
for m in range(M):
    tmp = -heapq.heappop(ls)
    tmp = tmp // 2
    heapq.heappush(ls, -tmp)
print(-sum(ls))
