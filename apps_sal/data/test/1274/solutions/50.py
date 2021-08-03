from heapq import heappop, heappush
n, m = map(int, input().split())
ab = [list(map(int, input().split()))for _ in range(n)] + [[100000000, 0]]
for i in range(m):
    ab.append([i + 1, 0])
ab.sort()
h = []
j = 0
ans = 0
for i in range(1, m + 1):
    while ab[j][0] <= i:
        heappush(h, -ab[j][1])
        j += 1
    ans -= heappop(h)
print(ans)
