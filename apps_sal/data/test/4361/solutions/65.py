N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]

H.sort()
ans = float("inf")

for i in range(N - K + 1):
    tmp = H[i + K - 1] - H[i]
    ans = min(ans, tmp)

print(ans)
