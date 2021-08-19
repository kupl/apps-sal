import heapq
(n, m) = map(int, input().split())
mm = 10 ** 5 + 5
c = [[0] for i in range(mm)]
for i in range(n):
    (a, b) = map(int, input().split())
    c[a].append(b)
ans = 0
h = []
for i in reversed(range(m)):
    d = m - i
    for j in c[d]:
        heapq.heappush(h, -j)
    ans += -heapq.heappop(h)
print(ans)
