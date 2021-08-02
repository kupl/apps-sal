def ll(): return list(map(int, input().split()))


testcases = 1
# testcases=int(input())
for testcase in range(testcases):
    s = input()
    n = len(s)
    dp = [0]
    # print(dp)
    for i in range(n - 1):
        if s[i] == 'v' and s[i + 1] == 'v':
            dp.append(dp[-1] + 1)
        else:
            dp.append(dp[-1])
    # print(dp)
    ans = 0
    for i in range(0, n):
        if s[i] == 'o':
            ans += (dp[i] * (dp[-1] - dp[i]))
    print(ans)
