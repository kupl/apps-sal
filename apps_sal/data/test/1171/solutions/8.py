from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
V = list(map(int, input().split()))
INF = 10**9


def h(X, cnt):
    S = sum(X)
    heapify(X)
    limit = cnt
    while cnt < K and cnt < 2 * limit:
        m = heappop(X)
        if m >= 0:
            break
        S -= m
        cnt += 1
    return S


ans = 0

for i in range(1, min(N, K) + 1):
    if i != N:
        for j in range(i + 1):
            X = V[:i - j] + V[N - j:]
            ans = max(ans, h(X, i))
    else:
        ans = max(ans, h(V, i))

print(ans)
