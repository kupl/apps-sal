import sys
n, m = list(map(int, input().split()))
w1 = []
w2 = []
w3 = [10**10]

for w, c in (list(map(int, l.split())) for l in sys.stdin):
    if w == 1:
        w1.append(c)
    elif w == 2:
        w2.append(c)
    else:
        w3.append(c)

w1.sort(reverse=True)
w2.sort(reverse=True)
w3.sort(reverse=True)
w3[0] = 0
w1_size, w2_size = len(w1), len(w2)

dp = [(0, 0, 0) for _ in range(m + 3)]
for i in range(m):
    dp[i + 1] = max(dp[i + 1], dp[i])
    if dp[i][1] < w1_size:
        dp[i + 1] = max(dp[i + 1], (dp[i][0] + w1[dp[i][1]], dp[i][1] + 1, dp[i][2]))
    if dp[i][2] < w2_size:
        dp[i + 2] = max(dp[i + 2], (dp[i][0] + w2[dp[i][2]], dp[i][1], dp[i][2] + 1))

ans = 0
w3_c = 0

for i in range(len(w3)):
    if i * 3 > m:
        continue
    w3_c += w3[i]
    ans = max(ans, w3_c + dp[m - i * 3][0])

print(ans)
