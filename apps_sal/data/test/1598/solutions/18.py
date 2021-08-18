s = input()
ans = list(s)
n = len(s)
dp = [0] * n
i = 0
j = 1
while j < n:
    if s[i] == "1" and s[j] == "0":
        dp[i] = 1
        dp[j] = 1
        if i > 0:
            while dp[i] == 1 and i > 0:
                i -= 1
        j += 1
    else:
        j += 1
        i = j - 1
for i in range(n):
    if dp[i] == 0:
        ans[i] = "0"
print("".join(ans))
