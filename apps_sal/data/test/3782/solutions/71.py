from heapq import heappush, heappop
(N, K, Q) = map(int, input().split())
A = list(map(int, input().split()))
ans = float('inf')
for x in A:
    data = []
    h = []
    for i in range(N):
        if A[i] >= x:
            heappush(h, A[i])
        elif h:
            data.append(h)
            h = []
    if h:
        data.append(h)
    lsls = []
    for h in data:
        for j in range(max(0, len(h) - K + 1)):
            lsls.append(heappop(h))
    lsls.sort()
    if len(lsls) >= Q:
        ans = min(ans, lsls[Q - 1] - lsls[0])
print(ans)
