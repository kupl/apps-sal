from math import inf
t = int(input())
for q in range(t):
    a, b, p = [int(i) for i in input().split()]
    s = input()
    l = len(s)
    dp = [0] * l
    if s[l - 2] == 'A':
        dp[l - 2] = a
    else:
        dp[l - 2] = b
    for i in range(l - 3, -1, -1):
        if s[i] == s[i + 1]:
            dp[i] = dp[i + 1]
        else:
            if s[i] == 'A':
                dp[i] = dp[i + 1] + a
            else:
                dp[i] = dp[i + 1] + b
    # print(dp)
    for i in range(l):
        if p >= dp[i]:
            print(i + 1)
            break
