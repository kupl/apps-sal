import heapq
(N, M) = map(int, input().split())
arr = list(map(int, input().split()))
hq = []
for i in arr:
    heapq.heappush(hq, -i)
while M > 0:
    a = heapq.heappop(hq)
    heapq.heappush(hq, a / 2)
    M -= 1
ans = 0
for i in hq:
    ans += int(-i)
print(ans)
