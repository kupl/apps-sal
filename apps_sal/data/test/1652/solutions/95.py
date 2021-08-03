import sys
input = sys.stdin.readline
S = input()[: -1]
dp = [0] * (len(S) + 1)
dp[0] = 1
for i in range(len(S)):
    if i + 5 <= len(S):
        if S[i: i + 5] == "dream":
            dp[i + 5] += dp[i]
        if S[i: i + 5] == "erase":
            dp[i + 5] += dp[i]
    if i + 7 <= len(S):
        if S[i: i + 7] == "dreamer":
            dp[i + 7] += dp[i]
    if i + 6 <= len(S):
        if S[i: i + 6] == "eraser":
            dp[i + 6] += dp[i]
if dp[-1]:
    print("YES")
else:
    print("NO")
