(N, K) = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))
h.sort()
ans = 10 ** 18
for i in range(N - K + 1):
    if h[i + K - 1] - h[i] < ans:
        ans = h[i + K - 1] - h[i]
print(ans)
