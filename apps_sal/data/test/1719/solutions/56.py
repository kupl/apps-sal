n = int(input())
x = 0
dp = [[[[0] * 4 for q in range(4)] for p in range(4)] for i in range(n - 2)]
ng = ['012', '021', '102', '0112', '0132', '0312']
for p in range(4):
    for q in range(4):
        for r in range(4):
            if str(p) + str(q) + str(r) not in ng:
                dp[0][p][q][r] += 1
for i in range(n - 3):
    for p in range(4):
        for q in range(4):
            for r in range(4):
                for s in range(4):
                    if str(p) + str(q) + str(r) + str(s) not in ng and str(q) + str(r) + str(s) not in ng:
                        dp[i + 1][q][r][s] += dp[i][p][q][r]
for p in range(4):
    for q in range(4):
        for r in range(4):
            x = (x + dp[-1][p][q][r]) % (10 ** 9 + 7)
print(x)
