import heapq
(n, m) = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))
heapq.heapify(a)
for i in range(m):
    heapq.heapreplace(a, a[0] / 2)
print(-sum(map(int, a)))
