import sys
t = int(input())
for e in range(t):

    n, x = list(map(int, input().split()))
    dp = [0 for i in range(n + 1)]
    s = input()
    cur = 0
    for i in range(n):
        if(s[i] == '0'):
            cur += 1
        else:
            cur -= 1
        dp[i + 1] = cur

    if(dp[-1] == 0):
        if(min(dp) <= x <= max(dp)):
            print(-1)
        else:
            print(0)
        continue
    cnt = 0
    for i in range(n):
        diff = x - dp[i]
        if((diff) * dp[-1] >= 0 and diff % dp[-1] == 0):
            cnt += 1
    print(cnt)
