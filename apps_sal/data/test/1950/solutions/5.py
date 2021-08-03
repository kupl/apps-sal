import heapq
n = int(input())
l = [int(i) for i in input().split()]
if n % 2 == 0:
    l = [0] + l
result = 0
heapq.heapify(l)
while len(l) > 1:
    x = heapq.heappop(l)
    y = heapq.heappop(l)
    z = heapq.heappop(l)
    result += x + y + z
    heapq.heappush(l, x + y + z)
print(result)
