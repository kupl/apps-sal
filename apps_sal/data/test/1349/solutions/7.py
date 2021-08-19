t = list(map(int, input().strip().split()))[0]
for i in range(t):
    (n, p) = list(map(int, input().strip().split()))
    dp = dict()
    for i in range(1, n + 1):
        dp[i] = 1
    k = list(map(int, input().strip().split()))
    plus = []
    minus = []
    for j in k:
        plus.append(j)
        minus.append(j)
    second = 0
    while len(dp) > 0:
        for i in plus:
            if i + second in dp:
                dp.pop(i + second)
        for i in minus:
            if i - second in dp:
                dp.pop(i - second)
        second += 1
    print(second)
