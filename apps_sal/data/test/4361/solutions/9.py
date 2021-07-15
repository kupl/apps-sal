N, K = map(int, input().split())
h = [0] * N
for i in range(N):
    h[i] = int(input())

h = sorted(h)
ans = 10**10
for i in range(N - K + 1):
    ans = min(ans, h[i + K - 1] - h[i])

print(ans)
