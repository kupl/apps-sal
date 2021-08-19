(n, k) = map(int, input().split(' '))
s = input()
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for l in range(0, n):
    for i in range(l, n + 1):
        used = [False] * 26
        for j in range(i + 1, n + 1):
            ch = ord(s[j - 1]) - ord('a')
            if not used[ch]:
                dp[l + 1][j] += dp[l][i]
                used[ch] = True
total = 0
for l in range(n, -1, -1):
    sums = sum(dp[l])
    if sums >= k:
        total += (n - l) * k
        k = 0
        break
    total += (n - l) * sums
    k -= sums
if k > 0:
    total = -1
print(total)
