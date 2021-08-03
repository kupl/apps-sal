n = int(input())
c = []
s = []
for _ in range(n):
    ln = input().split()
    c.append(int(ln[0]))
    s.append(str(ln[1]))
dp = [1e9 for _ in range(8)]
dp[0] = 0
for i in range(n):
    k = 0
    if 'A' in s[i]:
        k += 1
    if 'B' in s[i]:
        k += 2
    if 'C' in s[i]:
        k += 4
    for j in range(8):
        dp[j | k] = min(dp[j | k], dp[j] + c[i])
if dp[7] == 1e9:
    print(-1)
else:
    print(dp[7])
