N, K = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))
h.sort()
ans = 1000000000
for i in range(N - K + 1):
    ans = min(ans, h[i + K - 1] - h[i])
print(ans)
