from heapq import heapify, heappop, heappush
n, k = list(map(int, input().split()))
N = 2 * 10**5 + 2
segs = []
plus = [0 for _ in range(N)]
minus = [0 for _ in range(N)]
ans = []
heapmin = []
heapmax = []
for i in range(n):
    x, y = list(map(int, input().split()))
    heappush(heapmin, (x - 1, y - 1, i + 1))

height = 0
for i in range(N):
    height += plus[i]
    height -= minus[i]
    while len(heapmin) > 0 and heapmin[0][0] <= i:
        x, y, ii = heappop(heapmin)
        heappush(heapmax, (-y, x, ii))
        height += 1
        minus[y + 1] += 1
    while height > k:
        y, x, ii = heappop(heapmax)
        y = -y
        height -= 1
        plus[y + 1] += 1
        ans.append(ii)
print(len(ans))
print(*ans)
