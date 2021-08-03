mod = 10**9 + 7
n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()
if ab == "A" and aa == "A":
    print((1))
    return
if ab == "B" and bb == "B":
    print((1))
    return


# aa,ab,ba,bb
# A,B,(A,B),(A,B)
# B,A,(A,B),(A,B)

if (ab == "A" and ba == "A") or (ab == "B" and ba == "B"):
    # AAAAB+AAAAB+AAAB
    # (A*(1~) + B*1)*(1~)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n - 1):
        for j in range(2, n + 1):
            if j + i > n:
                break
            dp[i + j] += dp[i]
            dp[i + j] %= mod
    print((dp[n]))
    return

# AAAAA + BBBBB + AAAAA + BBBBB + AAAAA + B
# (A*(1~) + B*(1))*(1~) + A*(1~) + B*1

if True:
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n - 1):
        for j in range(2, n + 1):
            if j + i > n:
                break
            dp[i + j] += dp[i] * (j - 1)
            dp[i + j] %= mod
    ans = 0
    for i in range(n - 1):
        ans += dp[i]
        ans %= mod
    print(ans)
