n = int(input())
mod = pow(10, 9) + 7
memo = [{} for _ in range(n + 1)]


def judge(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            (t[i], t[i - 1]) = (t[i - 1], t[i])
        if ''.join(t).count('AGC') >= 1:
            return False
    return True


def dfs(cur, last3):
    if cur == n:
        return 1
    if last3 in memo[cur]:
        return memo[cur][last3]
    ans = 0
    for c in 'AGCT':
        if judge(last3 + c):
            ans = (ans + dfs(cur + 1, last3[1:] + c)) % mod
    memo[cur][last3] = ans
    return ans


print(dfs(0, 'TTT'))
