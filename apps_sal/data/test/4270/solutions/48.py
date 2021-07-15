import heapq
n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)

while len(h) >= 2:
  x = heapq.heappop(h)
  y = heapq.heappop(h)
  z = (x+y)/2.0
  heapq.heappush(h, z)

print(h[0])
