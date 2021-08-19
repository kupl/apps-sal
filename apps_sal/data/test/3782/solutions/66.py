import heapq
(N, K, Q) = map(int, input().split())
(*A,) = map(int, input().split())
ans = 10 ** 10
A.append(-1)
for y in A:
    if y == -1:
        break
    (p, q) = ([], [])
    for a in A:
        if a >= y:
            heapq.heappush(p, a)
        else:
            for i in range(max(0, len(p) - (K - 1))):
                heapq.heappush(q, heapq.heappop(p))
            p = []
    if len(q) < Q:
        continue
    x = -1
    for i in range(Q):
        x = heapq.heappop(q)
    ans = min(ans, x - y)
print(ans)
