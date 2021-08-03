MX = 1030
M = 1000 * 1000 * 1000 + 7
c = [[0] * MX for i in range(MX)]
for i in range(MX):
    c[i][0] = 1
for i in range(1, MX):
    for j in range(1, MX):
        c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
        c[i][j] %= M

num = list(map(int, list(input())))
cnt = int(input())
dp = [0] * MX
for i in range(2, MX):
    dp[i] = dp[bin(i).count('1')] + 1

if cnt == 0:
    print(1)
    return

res = 0

for i in range(1, MX):
    if dp[i] != cnt - 1:
        continue
    n = len(num) - 1
    k = i
    for pos in range(len(num)):
        if num[pos] == 1:
            # print(n, k)
            # if we put 0 here
            res += c[n][k]
            res %= M
            k -= 1
        n -= 1
    # print(k)
    if n == -1 and k == 0:
        res += 1
if cnt == 1:
    res -= 1
print(res)
