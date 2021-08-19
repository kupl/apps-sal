n = int(input())
d = input()
l = len(d)
dp = [[0, 0] for i in range(0, l + 1)]
dp[l - 1] = [ord(d[l - 1]) - ord('0'), 1]
for i in range(1, l):
    w = l - 1 - i
    m = (ord(d[w]) - ord('0')) * n ** i + dp[w + 1][0]
    dp[w] = [m, i + 1]
    if d[w] == '0':
        dp[w][0] = dp[w + 1][0]
        dp[w][1] = dp[w + 1][1] + 1
        continue
    for j in range(w, l):
        subs = int(d[w:j + 1])
        u = dp[j + 1]
        if subs < n:
            re = subs * n ** u[1] + u[0]
            if re < dp[w][0] or (re == dp[w][0] and 1 + u[1] < dp[w][1]):
                dp[w][0] = re
                dp[w][1] = 1 + u[1]
        else:
            break
print(dp[0][0])
