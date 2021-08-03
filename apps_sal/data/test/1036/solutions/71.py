N, k = map(int, input().split())
S = list(input())


def zyanken(a, b):
    if a == "R":
        if b == "P":
            return "P"
        else:
            return "R"
    elif a == "S":
        if b == "R":
            return "R"
        else:
            return "S"
    elif a == "P":
        if b == "S":
            return "S"
        else:
            return "P"


now = k
f = 0
dp = [["" for i in range(300)]for j in range(300)]
dp[0] = S
if N == 1:
    print(S[0])
else:
    for i in range(k):
        for j in range(N):
            dp[i + 1][j] = zyanken(dp[i][(j * 2) % N], dp[i][(j * 2 + 1) % N])
    print(dp[k][0])
