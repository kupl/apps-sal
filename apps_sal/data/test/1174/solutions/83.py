import heapq
n, m = map(int, input().split())
a = [i * -1 for i in list(map(int, input().split()))]
heapq.heapify(a)
for i in range(m):
    x = heapq.heappop(a) * -1
    heapq.heappush(a, (x // 2) * -1)
print(sum(a) * -1)
