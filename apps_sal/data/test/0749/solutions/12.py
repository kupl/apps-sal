S = input()
dp = [[1 for i in range(26)] for j in range(len(S))]
for i in range(len(S) - 2, -1, -1):
    dp[i] = [x + 1 for x in dp[i + 1]]
    dp[i][ord(S[i + 1]) - ord('a')] = 1
dp2 = [[1 for i in range(26)] for j in range(len(S))]
for i in range(1, len(S)):
    dp2[i] = [x + 1 for x in dp2[i - 1]]
    dp2[i][ord(S[i - 1]) - ord('a')] = 1
ans = [0 for i in range(26)]
for i in range(len(S)):
    k = ord(S[i]) - ord('a')
    ans[k] = max(ans[k], dp[i][k], dp2[i][k])
out = len(S)
for i in range(26):
    if ans[i]:
        out = min(out, ans[i])
print(out)
