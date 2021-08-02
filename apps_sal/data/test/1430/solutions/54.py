N, K = map(int, input().split())
S = input()
dp = []
p, q = 0, 0
for i in S:
    if i == '1':
        if 0 < q:
            dp.append(q)
        p += 1
        q = 0
    else:
        if 0 < p:
            dp.append(p)
        p = 0
        q += 1
if 0 < p:
    dp.append(p)
else:
    dp.append(q)
if S[0] == '0':
    if len(dp) <= 2 * K:
        print(sum(dp))
    else:
        if S[N - 1] == '0':
            dp.append(0)
        dp.insert(0, 0)
        ans = sum(dp[:2 * K + 1])
        bns = ans
        for i in range(2 * K, len(dp), 2):
            if i == 2 * K:
                continue
            bns += dp[i] + dp[i - 1] - dp[i - 2 * K - 1] - dp[i - 2 * K - 2]
            ans = max(ans, bns)
        print(ans)
else:
    if len(dp) <= 2 * K + 1:
        print(sum(dp))
    else:
        if S[N - 1] == '0':
            dp.append(0)
        ans = sum(dp[:2 * K + 1])
        bns = ans
        for i in range(2 * K, len(dp), 2):
            if i == 2 * K:
                continue
            bns += dp[i] + dp[i - 1] - dp[i - 2 * K - 1] - dp[i - 2 * K - 2]
            ans = max(ans, bns)
        print(ans)
