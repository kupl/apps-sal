n = int(input())
a = list(map(int, input().split()))

a = list(enumerate(a))
a.sort(key=lambda x: x[1])

# dp[left + right][left]
dp = [[] for _ in range(n + 1)]
dp[0].append(0)

for i in range(1, n + 1):  # i = left + right
    ind, act = a.pop(-1)

    # all right
    dp[i].append(dp[i - 1][0] + act * (n - i - ind))

    # middle
    for j in range(1, i):  # j = left
        ar = dp[i - 1][j] + act * (n - i + j - ind)  # rightに追加
        al = dp[i - 1][j - 1] + act * (ind - j + 1)  # leftに追加
        dp[i].append(max([ar, al]))

    # all left
    dp[i].append(dp[i - 1][i - 1] + act * (ind - i + 1))

print(max(dp[n]))
