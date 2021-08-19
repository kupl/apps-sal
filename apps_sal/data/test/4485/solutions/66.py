(N, M) = map(int, input().strip().split())
dp = [0 for _ in range(N)]
find = False
for _ in range(M):
    (a, b) = map(int, input().strip().split())
    if a == 1:
        dp[b - 1] += 1
    elif a == N:
        dp[b - 1] += 1
    if b == 1:
        dp[a - 1] += 1
    elif b == N:
        dp[a - 1] += 1
    if dp[a - 1] == 2 or dp[b - 1] == 2:
        find = True
        break
print('POSSIBLE' if find == True else 'IMPOSSIBLE')
