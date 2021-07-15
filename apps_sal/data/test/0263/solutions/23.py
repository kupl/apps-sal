import heapq
N = int(input())
M = int(input())
src = [int(input()) for i in range(N)]

mx = max(src) + M

hq = src[:]
heapq.heapify(hq)

for i in range(M):
    m = heapq.heappop(hq)
    heapq.heappush(hq, m+1)
while hq:
    mn = heapq.heappop(hq)

print(mn, mx)

