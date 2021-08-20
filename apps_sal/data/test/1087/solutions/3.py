(N, K) = list(map(int, input().split()))
L = list(map(int, input().split()))
d = format(K, 'b')
dp = [[-1 for _ in range(2)] for _ in range(len(d) + 1)]
dp[0][0] = 0
for i in range(len(d))[::-1]:
    if K == 0:
        break
    index = len(d) - i - 1
    cnt = 0
    for x in L:
        if x & 1 << i:
            cnt += 1
    tmp = 2 ** i
    if dp[index][1] != -1:
        dp[index + 1][1] = max(dp[index + 1][1], dp[index][1] + max(cnt, N - cnt) * tmp)
    if d[index] == '1':
        if dp[index][0] != -1:
            dp[index + 1][1] = max(dp[index + 1][1], dp[index][0] + cnt * tmp)
        if dp[index][0] != -1:
            dp[index + 1][0] = max(dp[index + 1][0], dp[index][0] + (N - cnt) * tmp)
    elif dp[index][0] != -1:
        dp[index + 1][0] = max(dp[index + 1][0], dp[index][0] + cnt * tmp)
ans = 0
for i in range(len(d), 50):
    tmp = 2 ** i
    cnt = 0
    for x in L:
        if x & 1 << i:
            cnt += 1
    ans += cnt * tmp
print(ans + max(dp[len(d)][0], dp[len(d)][1], 0))
