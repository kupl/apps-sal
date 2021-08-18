N, K = map(int, input().split())

H = sorted([int(input()) for _ in range(N)])

ans = H[K - 1] - H[0]

for k in range(N - K + 1):
    ans = min(ans, H[k + K - 1] - H[k])

print(ans)
