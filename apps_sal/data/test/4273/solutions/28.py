import math
'\nint(input())\nmap(int, input().split())\nlist(map(int, input().split()))\ninput()\ninput().split()\n'
n = int(input())
ans = 0
dp = [0, 0, 0, 0, 0]
for i in range(n):
    s = input()
    if s[0] == 'M':
        dp[0] += 1
    elif s[0] == 'A':
        dp[1] += 1
    elif s[0] == 'R':
        dp[2] += 1
    elif s[0] == 'C':
        dp[3] += 1
    elif s[0] == 'H':
        dp[4] += 1
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += dp[i] * dp[j] * dp[k]
print(ans)
