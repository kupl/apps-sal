t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    dp = [0 for i in range(n)]
    dp[-1] = 1
    for i in range(n - 2, -1, -1):
        if li[i] == 1:
            dp[i] = 3 - dp[i + 1]
        else:
            dp[i] = 1
    if dp[0] == 1:
        print('First')
    else:
        print('Second')
