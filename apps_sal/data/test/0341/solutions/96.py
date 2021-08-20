(N, K) = map(int, input().split())
RSP = list(map(int, input().split()))
T = input()
dp = [[0] * 3 for _ in range(N + 1)]


def judge(a, b):
    if a == 'r' and b == 2:
        return RSP[2]
    elif a == 's' and b == 0:
        return RSP[0]
    elif a == 'p' and b == 1:
        return RSP[1]
    return 0


for i in range(1, N + 1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - K][k] + judge(T[i - 1], j))
ans = 0
for k in range(K):
    ans += max(dp[N - k])
print(ans)
