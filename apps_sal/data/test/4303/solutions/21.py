N, K = map(int, input().split())
x = list(map(int, input().split()))

tp = N
for i in range(N):
    if x[i] >= 0:
        tp = i
        break
    x[i] *= -1

s = max(0, tp - K + 1)
g = min(tp - 1, N - K)

ans = float("INF")
if K <= tp:
    ans = min(ans, x[tp - K])
if K <= N - tp:
    ans = min(ans, x[tp + K - 1])

for i in range(s, g + 1):
    ans = min(ans, x[i] + x[i + K - 1] + min(x[i], x[i + K - 1]))
    #print(x[i], x[i+K-1])

print(ans)
