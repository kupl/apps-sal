test = int(input())
for _ in range(test):
    n, a, b = map(int, input().split())
    s = input()
    ans = a * n + b * (n + 1)
    for i in range(n):
        if s[n - i - 1] == '1':
            s = s[:n - i]
            break
    for i in range(len(s)):
        if s[i] == '1':
            s = s[i:]
            break
    if s.count('1') == 0:
        print(ans)
        continue
    dp = []
    c = 1
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            c += 1
        else:
            dp.append(c)
            c = 1
    dp.append(c)
    for i in dp[::2]:
        ans += (i + 1) * b
    ans += len(dp[::2]) * a * 2
    for i in dp[1::2]:
        if (i - 1) * b < 2 * a:
            ans += (i - 1) * b
            ans -= 2 * a
    print(ans)
