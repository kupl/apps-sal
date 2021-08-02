import heapq
n = int(input())
a = [int(i) for i in input().split()]
heapq.heapify(a)
if (n & 1) == 0:
    heapq.heappush(a, 0)
res = 0
while len(a) > 1:
    s = heapq.heappop(a) + heapq.heappop(a) + heapq.heappop(a)
    res += s
    heapq.heappush(a, s)
print(res)
