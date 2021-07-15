from sys import stdin, stdout

n = int(stdin.readline())
dp = [[0 for i in range(n + 10)] for j in range(n + 10)]

MOD = 10 ** 9 + 7
dp[-1][0] = 1
previous = []

for i in range(n):
    s = stdin.readline().strip()
    
    if not previous or previous[-1] != 'f':
        cnt = 0
            
        for j in range(n, -1, -1):
            cnt = (cnt + dp[i - 1][j]) % MOD
            dp[i][j] = cnt
    else:
        cnt = 0
            
        for j in range(n + 1, -1, -1):
            cnt = dp[i - 1][j - 1]
            dp[i][j] = cnt
    
    previous.append(s)

ans = 0
for i in range(n + 1):
    ans = (ans + dp[n - 1][i]) % MOD

stdout.write(str(ans))
