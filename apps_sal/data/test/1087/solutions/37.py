(N, K) = map(int, input().split())
A = list(map(int, input().split()))
cnts = [0] * 46
for a in A:
    for i in range(46):
        if a & 1 << i:
            cnts[i] += 1
L = 45
dp = [[-1 for _ in range(2)] for _ in range(L + 1)]
dp[0][0] = 0
for i in range(L):
    p0 = pow(2, L - 1 - i) * cnts[L - 1 - i]
    p1 = pow(2, L - 1 - i) * (N - cnts[L - 1 - i])
    if K & 1 << L - 1 - i:
        is_one = True
    else:
        is_one = False
    if dp[i][1] != -1:
        dp[i + 1][1] = dp[i][1] + max(p0, p1)
    if dp[i][0] != -1 and is_one:
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + p0)
    if dp[i][0] != -1:
        if is_one:
            dp[i + 1][0] = dp[i][0] + p1
        else:
            dp[i + 1][0] = dp[i][0] + p0
print(max(dp[-1]))
