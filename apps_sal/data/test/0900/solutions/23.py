S = [int(x) if x != "?" else -1 for x in input()]
g = 10 ** 9 + 7
x = 1
DP = [[0] * 13 for _ in range(2)]
DP[0][0] = 1
for i in range(len(S)):
    for j in range(13):
        DP[1][j] = DP[0][j] % g
        DP[0][j] = 0
    for j in range(13):
        if S[i] == -1:
            s = (j * 10) % 13
            e = (s + 10) % 13
        else:
            s = (j * 10 + S[i]) % 13
            e = (s + 1) % 13
        DP[0][s] += DP[1][j]
        if s > e:
            DP[0][0] += DP[1][j]
        DP[0][e] -= DP[1][j]
    w = 0
    for j in range(13):
        w += DP[0][j]
        DP[0][j] = w

print((DP[0][5] % g))
