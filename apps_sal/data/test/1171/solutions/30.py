import bisect
(N, K) = list(map(int, input().split()))
V = list(map(int, input().split()))
ans = 0
for i in range(1, K + 1):
    nownow = 0
    for p in range(i + 1):
        if i < N:
            now = sorted(V[:p] + V[p + N - i:])
        else:
            now = V
        index = bisect.bisect_right(now, 0)
        if K - i >= index:
            nownow = sum(now[index:])
        else:
            nownow = sum(now[K - i:])
        ans = max(ans, nownow)
print(ans)
