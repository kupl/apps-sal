import heapq
n, m, *a = list(map(int, open(0).read().split()))
a = list([-x for x in a])

heapq.heapify(a)
for i in range(m):
    b = -heapq.heappop(a)
    heapq.heappush(a, -(b >> 1))

print((-sum(a)))

