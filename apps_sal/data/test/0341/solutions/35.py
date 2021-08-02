n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
dp = [0] * (len(t) + 1)
dp[0] = 0


def pon(d):
    if d == 'r':
        return p
    elif d == 's':
        return r
    else:
        return s


m = []
for i, j in enumerate(t):
    m.append(j)
    if i >= k:
        if m[i - k] == j:
            dp[i + 1] = dp[i]
            m[i] = 'skip'
        else:
            dp[i + 1] = dp[i] + pon(j)
    else:
        dp[i + 1] = dp[i] + pon(j)
print(dp[-1])
