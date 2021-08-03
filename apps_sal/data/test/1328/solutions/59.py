n, ma, mb = map(int, input().split())
med = [tuple(map(int, input().split())) for _ in range(n)]
maa = sum(x[0] for x in med)
mab = sum(x[1] for x in med)
dp = [[10**6] * (mab + 1) for _ in range(maa + 1)]
dp[0][0] = 0
for a, b, c in med:
    for i in range(maa, a - 1, -1):
        for j in range(mab, b - 1, -1):
            if dp[i][j] > dp[i - a][j - b] + c:
                dp[i][j] = dp[i - a][j - b] + c
mi = min(dp[ma * i][mb * i] for i in range(1, min(maa // ma, mab // mb) + 1))
if mi > 10**5:
    mi = -1
print(mi)
