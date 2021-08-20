import heapq
N = int(input())
a = list(map(int, input().split()))
lq = []
lsum = 0
rq = []
rsum = 0
for i in range(N):
    heapq.heappush(lq, a[i])
    lsum += a[i]
    heapq.heappush(rq, -1 * a[3 * N - 1 - i])
    rsum += a[3 * N - 1 - i]
llis = []
rlis = []
for i in range(N + 1):
    llis.append(lsum)
    rlis.append(rsum)
    heapq.heappush(lq, a[N + i])
    heapq.heappush(rq, -1 * a[2 * N - 1 - i])
    lsum += a[N + i]
    rsum += a[2 * N - 1 - i]
    lpop = heapq.heappop(lq)
    rpop = -1 * heapq.heappop(rq)
    lsum -= lpop
    rsum -= rpop
rlis.reverse()
ans = -1 * float('inf')
for i in range(N + 1):
    ans = max(ans, llis[i] - rlis[i])
print(ans)
