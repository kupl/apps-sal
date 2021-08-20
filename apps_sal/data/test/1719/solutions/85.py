(n, mod) = (int(input()), 10 ** 9 + 7)
dp = [{} for i in range(n + 1)]


def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            (t[i - 1], t[i]) = (t[i], t[i - 1])
        if ''.join(t).count('AGC') >= 1:
            return 0
    return 1


def dfs(cur, last3):
    if last3 in dp[cur]:
        return dp[cur][last3]
    if cur == n:
        return 1
    ret = 0
    for c in 'AGCT':
        if ok(last3 + c):
            ret += dfs(cur + 1, last3[1:] + c)
            ret %= mod
    dp[cur][last3] = ret
    return ret


print(dfs(0, 'TTT'))
