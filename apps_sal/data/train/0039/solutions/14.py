t = int(input())
for _ in range(t):
    (a, b, p) = map(int, input().split())
    s = input()
    n = len(s)
    dp = [0] * n
    for i in range(n - 2, -1, -1):
        if i == n - 2:
            dp[i] = a if s[i] == 'A' else b
        elif s[i] == s[i + 1]:
            dp[i] = dp[i + 1]
        else:
            dp[i] = dp[i + 1] + (a if s[i] == 'A' else b)
    ans = -1
    for i in range(n):
        if dp[i] <= p:
            ans = i + 1
            break
    print(ans)
