n = int(input())
s = input()
lens = len(s)
dp = [[0] * 5 for _ in range(lens + 5)]
parent = [[0] * 5 for _ in range(lens + 5)]
R, G, B = 1, 2, 3
sss = "0RGB"

dp[0][R] = dp[0][G] = dp[0][B] = 1
if s[0] == "R":
    dp[0][R] = 0
if s[0] == "G":
    dp[0][G] = 0
if s[0] == "B":
    dp[0][B] = 0

for i in range(1, lens):
    dp[i][R] = min(dp[i - 1][G], dp[i - 1][B]) + 1
    if dp[i][R] == dp[i - 1][G] + 1:
        parent[i][R] = G
    else:
        parent[i][R] = B

    dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + 1
    if dp[i][G] == dp[i - 1][R] + 1:
        parent[i][G] = R
    else:
        parent[i][G] = B

    dp[i][B] = min(dp[i - 1][G], dp[i - 1][R]) + 1
    if dp[i][B] == dp[i - 1][G] + 1:
        parent[i][B] = G
    else:
        parent[i][B] = R

    if s[i] == "R":
        dp[i][R] -= 1
    elif s[i] == "G":
        dp[i][G] -= 1
    elif s[i] == "B":
        dp[i][B] -= 1

ans = min(dp[lens - 1][R], dp[lens - 1][G], dp[lens - 1][B])
print(min(dp[lens - 1][R], dp[lens - 1][G], dp[lens - 1][B]))

ans2 = [0] * lens
if ans == dp[lens - 1][R]:
    i = lens - 1
    pp = R
    while i >= 0:
        ans2[i] = sss[pp]
        pp = parent[i][pp]
        i -= 1
elif ans == dp[lens - 1][G]:
    i = lens - 1
    pp = G
    while i >= 0:
        ans2[i] = sss[pp]
        pp = parent[i][pp]
        i -= 1
else:
    i = lens - 1
    pp = B
    while i >= 0:
        ans2[i] = sss[pp]
        pp = parent[i][pp]
        i -= 1

print("".join(ans2))
