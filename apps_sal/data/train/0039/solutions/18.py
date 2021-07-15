for i in range(int(input())):
    a, b, p = map(int, input().split())
    s = input()
    dp = [0 for i in range(len(s))]
    for j in range(len(s) - 2, -1, -1):
        if s[j] != s[j + 1] or dp[j + 1] == 0:
            if s[j] == 'B':
                if dp[j + 1] == 0:
                    dp[j] = b
                else:
                    dp[j] = dp[j + 1] + b
            else:
                if dp[j + 1] == 0:
                    dp[j] = a
                else:
                    dp[j] = dp[j + 1] + a
        else:
            dp[j] = dp[j + 1]
    ans = 1
    for i in dp:
        if i > p:
            ans += 1
        else:
            break
    print(ans)
