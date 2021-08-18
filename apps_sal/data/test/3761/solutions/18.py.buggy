import sys
s = input()
x, y = map(int, input().split())
s = s + 'T'
dp = [[] for i in range(2)]
t = 0
buf = 0
for j in range(len(s)):
    if s[j] == 'T':
        break

for i in range(j, len(s)):
    if s[i] == 'F':
        buf += 1
    else:
        if buf != 0:
            dp[t].append(buf)
            buf = 0
        t = 1 - t
# print(s)
# print(dp)
xb = 1 << (len(s) + j)
yb = 1 << (len(s))

for i in range(len(dp[0])):
    xb = (xb << dp[0][i]) | (xb >> dp[0][i])
if xb & 1 << (len(s) + x) == 0:
    print('No')
    return
for i in range(len(dp[1])):
    yb = (yb << dp[1][i]) | (yb >> dp[1][i])

if yb & 1 << (len(s) + y) == 0:
    print('No')
    return
print('Yes')
