import heapq
n = int(input())
heap = list(map(int, input().split())) + ([0] if n % 2 == 0 else [])
n = len(heap)
heapq.heapify(heap)
ans = 0
for i in range(n, 1, -2):
    x = heapq.heappop(heap) + heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, x)
    ans += x
print(ans)
