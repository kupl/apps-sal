(n, k) = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0] * 50
L = format(k, 'b').zfill(50)
S = [[0, 0] for _ in range(50)]
for a in A:
    a_ = format(a, 'b').zfill(50)
    for i in range(50):
        if a_[i] == '1':
            S[i][0] += 1
        else:
            S[i][1] += 1
for i in range(len(S)):
    S[i][0] *= pow(2, 50 - i - 1)
    S[i][1] *= pow(2, 50 - i - 1)
dp = [[-1, -1] for _ in range(55)]
dp[0][0] = 0
for i in range(50):
    if L[i] == '1':
        if dp[i][1] != -1:
            dp[i + 1][1] = dp[i][1] + max(S[i][0], S[i][1])
        if dp[i][0] != -1:
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + S[i][0])
            dp[i + 1][0] = dp[i][0] + S[i][1]
    else:
        if dp[i][1] != -1:
            dp[i + 1][1] = dp[i][1] + max(S[i][1], S[i][0])
        if dp[i][0] != -1:
            dp[i + 1][0] = dp[i][0] + S[i][0]
print(max(dp[50]))
