import heapq
n = int(input())
a = list(map(int, input().split()))

l_sum = [0 for _ in range(n+1)]
r_sum = [0 for _ in range(n+1)]

que = a[:n]
l_sum[0] = sum(que)
heapq.heapify(que)

for i in range(n):
    l_sum[i+1] = l_sum[i]

    if que[0] < a[n+i]:
        l_sum[i+1] += a[n+i] - que[0]
        heapq.heappop(que)
        heapq.heappush(que, a[n+i])


que = [-a[i] for i in range(2*n, 3*n)]
r_sum[0] = -sum(que)
heapq.heapify(que)

for i in range(n):
    r_sum[i+1] = r_sum[i]
    
    if -que[0] > a[2*n-1-i]:
        r_sum[i+1] += a[2*n-1-i] + que[0]
        heapq.heappop(que)
        heapq.heappush(que, -a[2*n-1-i])


ans = -1e15
for x in range(n+1):
    ans = max(ans, l_sum[x] - r_sum[n-x])

print(ans)
