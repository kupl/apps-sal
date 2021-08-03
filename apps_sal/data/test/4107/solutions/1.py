def get(n, k, s):
    nxt = [0] * (n + 1)
    cur = 1 << 30
    for i in range(n, 0, -1):
        if s[i - 1] == '1':
            cur = i
        nxt[i] = cur

    dp = [0]
    for i in range(1, n + 1):
        dp.append(dp[-1] + i)
        c = nxt[max(i - k, 1)]
        if c <= i + k:
            dp[i] = min(dp[i], dp[max(1, c - k) - 1] + c)

    return dp[n]


n, k = list(map(int, input().split()))
s = input()
print(get(n, k, s))
