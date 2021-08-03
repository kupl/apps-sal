from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))
heapify(a)
# print(a)

for i in range(m):
    x = -heappop(a)
    x //= 2
    heappush(a, -x)
print(-sum(a))
