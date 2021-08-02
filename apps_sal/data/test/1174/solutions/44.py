from heapq import *
n, m = map(int, input().split())
a = list(map(int, input().split()))

heap = []
for i in a:
    heappush(heap, -i)

for _ in range(m):
    tmp = heappop(heap)
    heappush(heap, -(-tmp // 2))

ans = 0
for a in heap:
    ans += -a
print(ans)
