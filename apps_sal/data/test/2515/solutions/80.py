dp = [1] * (10**5 + 1)  # エラトステネスの篩
dp[0], dp[1] = 0, 0
for i in range(2, 10**5 + 1):
    if dp[i] == 0:
        continue
    j = i
    while j + i <= 10**5:
        j += i
        if dp[j] == 1:
            dp[j] = 0

ni = [0] * (10**5 + 1)  # 2012_like check
for i in range(2, 10**5 + 1):
    if dp[i] == 1 and dp[(i + 1) // 2] == 1:
        ni[i] = 1

ru = [0] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    ru[i] = ru[i - 1] + ni[i]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(ru[r] - ru[l - 1])
