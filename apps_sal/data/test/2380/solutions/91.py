

import heapq

n, m = list(map(int, input().strip().split()))

q = []
a = list(map(int, input().strip().split()))
for i in range(n):
    heapq.heappush(q, (a[i] * (-1), 1))
for i in range(m):
    b, c = list(map(int, input().strip().split()))
    heapq.heappush(q, (c * (-1), b))

res = 0
for _ in range(n):
    c, b = heapq.heappop(q)
    res += c * (-1)
    if b > 1:
        b -= 1
        heapq.heappush(q, (c, b))

print(res)
