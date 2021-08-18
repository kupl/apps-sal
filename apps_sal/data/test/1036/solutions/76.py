n, k = list(map(int, input().split()))
s = list(input())


def f(a, b):
    p = set(["R", "S"])
    q = set(["P", "R"])
    r = set(["S", "P"])
    if a == b:
        return a
    elif (a in p) and (b in p):
        return "R"
    elif (a in q) and (b in q):
        return "P"
    elif (a in r) and (b in r):
        return "S"


dp = [[0] * (n) for i in range(k + 1)]

for i in range(n):
    dp[0][i] = s[i]

for i in range(1, k + 1):
    for j in range(n):
        dp[i][j] = f(dp[i - 1][j], dp[i - 1][(j + pow(2, i - 1)) % n])

print((dp[k][0]))
