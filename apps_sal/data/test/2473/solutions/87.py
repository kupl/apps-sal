(N, K) = list(map(int, input().split()))
point = [tuple(map(int, input().split())) for i in range(N)]
point.sort(key=lambda x: x[0])
ans = float('inf')
for i in range(1 + N - K):
    for j in range(i + K, N + 1):
        x = point[j - 1][0] - point[i][0]
        now = point[i:j]
        now.sort(key=lambda x: x[1])
        for k in range(j - i - K + 1):
            ans = min(x * (now[k + K - 1][1] - now[k][1]), ans)
print(ans)
