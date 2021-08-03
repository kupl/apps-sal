N, K = map(int, input().split())
lsh = [int(input()) for _ in range(N)]
lsh.sort()
ans = 10**9
for i in range(N - K + 1):
    ans = min(ans, lsh[i + K - 1] - lsh[i])
print(ans)
