import heapq

N, K = map(int, input().split())

V = list(map(int, input().split()))

ans = 0
for i in range(1, K+1):
    if i > N:
        continue
    for j in range(i+1):
        tmp = 0
        q = V[:j] + V[N-i+j:]
        heapq.heapify(q)
        for _ in range(min(i, K-i)):
            tmp_min = heapq.heappop(q)
            ans = max(ans, sum(q))
            if tmp_min > 0:
                ans = max(ans, sum(q)+tmp_min)
                break
        ans = max(ans, sum(q))

print(ans)
