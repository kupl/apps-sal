(n, l, r) = map(int, input().split())
ost0 = r // 3 - (l - 1) // 3
ost1 = ost0
if l % 3 == 0:
    ost2 = ost0 - 1
if l % 3 == 1:
    ost2 = ost0
if l % 3 == 2:
    ost2 = ost0
if r % 3 == 2:
    ost2 += 1
if l % 3 == 0:
    ost1 = ost2
if l % 3 == 1:
    ost1 = ost2
if l % 3 == 2:
    ost1 = ost2 - 1
if r % 3 == 1:
    ost1 += 1
dp = []
for i in range(n):
    dp.append([0, 0, 0])
(dp[0][0], dp[0][1], dp[0][2]) = (ost0, ost1, ost2)
mmm = [ost0, ost1, ost2]
for i in range(1, n):
    for j in range(3):
        dp[i][j] = (dp[i - 1][0] * mmm[j] + dp[i - 1][1] * mmm[(j - 1) % 3] + dp[i - 1][2] * mmm[(j - 2) % 3]) % (10 ** 9 + 7)
print(dp[-1][0] % (10 ** 9 + 7))
