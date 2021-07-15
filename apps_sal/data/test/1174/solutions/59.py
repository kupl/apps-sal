import heapq
n, m = [int(i) for i in input().split()]
a = [-int(i) for i in input().split()]
heapq.heapify(a)
for _ in range(m):
  value = heapq.heappop(a)
  value /= 2
  heapq.heappush(a, value)
for i in range(n):
  a[i] = int(-a[i])
print(sum(a))
