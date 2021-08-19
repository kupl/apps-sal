def check(i, bob):
    if i >= n:
        return (0, 0)
    if dp[bob][i] != (-1, -1):
        return dp[bob][i]
    if bob:
        x = check(i + 1, False)
        y = check(i + 1, True)
        if x[0] + arr[i] >= y[0]:
            ret = (x[0] + arr[i], x[1])
        else:
            ret = (y[0], y[1] + arr[i])
    else:
        x = check(i + 1, True)
        y = check(i + 1, False)
        if x[1] + arr[i] >= y[1]:
            ret = (x[0], x[1] + arr[i])
        else:
            ret = (y[0] + arr[i], y[1])
    dp[bob][i] = ret
    return ret


n = int(input())
dp = [(-1, -1)] * n
dp = [dp, dp.copy()]
arr = list(map(int, input().split()))
ans = check(0, True)
print(ans[1], ans[0])
