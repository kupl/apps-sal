def win(a, b):
    w = a
    if a == 'R' and b == 'P':
        w = b
    if a == 'P' and b == 'S':
        w = b
    if a == 'S' and b == 'R':
        w = b
    return w


(n, k) = list(map(int, input().split()))
dp = [[c for c in input()]]
for i in range(k):
    dp.append([*dp[i]])
    for j in range(n):
        dp[i + 1][j] = win(dp[i][j * 2 % n], dp[i][(j * 2 + 1) % n])
print(dp[k][0])
