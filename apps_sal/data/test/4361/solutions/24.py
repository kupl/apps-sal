(N, K) = map(int, input().split())
H = sorted([int(input()) for n in range(N)])
ans = H[-1] - H[0]
for n in range(N - K + 1):
    ans = min(ans, H[n + K - 1] - H[n])
print(ans)
