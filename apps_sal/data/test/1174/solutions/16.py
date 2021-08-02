import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] *= -1

heapq.heapify(a)

for i in range(m):
    ref = heapq.heappop(a) * -1
    ref //= 2
    heapq.heappush(a, -ref)

print(sum(a) * -1)
