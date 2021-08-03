H, N = list(map(int, input().split()))
magics = [list(map(int, input().split())) for _ in range(N)]

max_A = max(a for a, b in magics)
INF = 10**10
DP = [INF] * (H + max_A)
DP[0] = 0

for i in range(1, H + max_A):
    DP[i] = min(DP[i - a] + b for a, b in magics)

ans = min(DP[H:])
print(ans)
