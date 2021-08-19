#fin = open("input.txt")
s = input()  # fin.readline()
P, M = s.count("+"), s.count("-")
s = input()  # fin.readline()
p, m = s.count("+"), s.count("-")
if (m > M or p > P):
    print(0)
else:
    r = P + M - (p + m)
    dp = [[0.0] * (r + 1) for i in range(r + 1)]
    dp[0][0] = 1
    for i in range(1, r + 1):
        for j in range(i + 1):
            #print(i, j)
            if j - 1 >= 0:
                #print(dp[i - j][j - 1])
                dp[i - j][j] += dp[i - j][j - 1] / 2
            if i - j - 1 >= 0:
                #print(dp[i - j - 1][j])
                dp[i - j][j] += dp[i - j - 1][j] / 2
    print(dp[P - p][M - m])
