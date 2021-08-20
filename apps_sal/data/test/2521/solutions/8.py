import heapq
n = int(input())
A = list(map(int, input().split()))
sa = 0
sb = 0
hf = []
hb = []
la = [[0] * 2 for i in range(n + 1)]
for i in range(n):
    sa += A[i]
    heapq.heappush(hf, A[i])
for i in range(2 * n, 3 * n):
    sb += A[i]
    heapq.heappush(hb, -A[i])
la[0][0] = sa
la[-1][-1] = sb
for i in range(n, 2 * n):
    now = A[i]
    now2 = A[-1 - i]
    heapq.heappush(hf, now)
    heapq.heappush(hb, -now2)
    h1 = heapq.heappop(hf)
    h2 = -heapq.heappop(hb)
    sa += now - h1
    sb += now2 - h2
    la[i - n + 1][0] = sa
    la[-i + n - 2][1] = sb
ans = -float('INF')
for (i, j) in la:
    ans = max(ans, i - j)
print(ans)
