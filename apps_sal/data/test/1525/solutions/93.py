def f(i):
    if i == w - 1:
        for j in range(w - 2):
            if s[j] == s[j + 1] == 1:
                return
        nonlocal x
        for j in range(w):
            if j == 0:
                if s[0] == 1:
                    x[0][1] += 1
                else:
                    x[0][0] += 1
            elif j == w - 1:
                if s[w - 2] == 1:
                    x[w - 1][w - 2] += 1
                else:
                    x[w - 1][w - 1] += 1
            else:
                if s[j - 1] == 1:
                    x[j][j - 1] += 1
                elif s[j] == 1:
                    x[j][j + 1] += 1
                else:
                    x[j][j] += 1
        return
    s[i] = 1
    f(i + 1)
    s[i] = 0
    f(i + 1)


h, w, k = map(int, input().split())
mod = pow(10, 9) + 7
s = [0] * (w - 1)
x = [[0] * w for _ in range(w)]
if not w == 1:
    f(0)
else:
    print(1)
    return
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
for i in range(1, h + 1):
    for j in range(w):
        for l in range(w):
            dp[i][j] += dp[i - 1][l] * x[l][j]
            dp[i][j] %= mod
print(dp[h][k - 1])
