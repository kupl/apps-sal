import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return map(int, sys.stdin.readline().split())


def SI():
    return sys.stdin.readline().strip()


t = II()
for q in range(t):
    n = II()
    a = LI()
    d = [[] for i in range(n + 1)]
    d2 = [0] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(n):
        if d2[a[i]] == 0:
            d2[a[i]] = 1
            d[a[i]].append(i)
            dp[a[i]] = i + 1
        else:
            d2[a[i]] += 1
            dp[a[i]] = max(dp[a[i]], i - d[a[i]][-1])
            d[a[i]].append(i)
    for i in range(n):
        dp[a[i]] = max(dp[a[i]], n - d[a[i]][-1])
    ans = [-1] * (n + 1)
    temp = -1
    for i in range(n + 1):
        if ans[dp[i]] == -1:
            ans[dp[i]] = i
    temp = -1
    for i in range(1, n + 1):
        if ans[i] != -1:
            if temp == -1:
                temp = ans[i]
            elif ans[i] < temp:
                temp = ans[i]
            else:
                ans[i] = temp
        else:
            ans[i] = temp
    print(*ans[1:])
