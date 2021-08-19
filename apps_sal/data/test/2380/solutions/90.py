from heapq import *
(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
h = []
for a in A:
    heappush(h, (-1 * a, 1))
for _ in range(m):
    (b, c) = list(map(int, input().split()))
    heappush(h, (-1 * c, b))
ans = 0
for _ in range(len(A)):
    (c, b) = heappop(h)
    ans += -1 * c
    if b > 1:
        heappush(h, (c, b - 1))
print(ans)
