N = int(input())
maxs = 0
s = []
for i in range(N):
    cin = int(input())
    s.append(cin)
    maxs = max(maxs, cin)
M = maxs * N
dp = [False] * (M + 1)
dp[0] = True
for x in s:
    for i in range(M + 1):
        if M - i < x:
            continue
        if dp[M - i - x]:
            dp[M - i] = True
for i in range(M + 1):
    if (M - i) % 10 != 0 and dp[M - i]:
        print(M - i)
        break
else:
    print(0)
