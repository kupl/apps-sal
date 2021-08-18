import heapq
n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]
ab = list(sorted(ab, key=lambda x: x[0]))

hq = []
ans = 0
j = 0
for i in range(1, m + 1):
    while (j < n) and (ab[j][0] <= i):
        heapq.heappush(hq, -ab[j][1])
        j += 1
    if len(hq):
        ans += -heapq.heappop(hq)

print(ans)
