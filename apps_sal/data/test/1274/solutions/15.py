import heapq

n, m = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)

c = []
ans = 0
for i in range(m):
    while len(ab) != 0 and ab[-1][0] <= i + 1:
        _, b = ab.pop()
        heapq.heappush(c, -b)
    if c:
        ans += -heapq.heappop(c)
print(ans)
