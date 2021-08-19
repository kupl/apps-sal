import sys
import math
import queue
import bisect
MOD = 10 ** 9 + 7
sys.setrecursionlimit(1000000)
(n, m) = map(int, input().split())
(c1, c2, c3) = ([0], [0], [0])
for _ in range(n):
    (x, y) = map(int, input().split())
    if x == 3:
        c3.append(y)
    elif x == 2:
        c2.append(y)
    else:
        c1.append(y)
c1.sort(reverse=True)
c2.sort(reverse=True)
c3.sort(reverse=True)
dp = [None for i in range(m + 1)]
dp[0] = (0, 0, 0)
dp[1] = (c1[0], 1, 0)
for i in range(2, m + 1):
    if dp[i - 1][1] == len(c1):
        x1 = (dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    else:
        x1 = (dp[i - 1][0] + c1[dp[i - 1][1]], dp[i - 1][1] + 1, dp[i - 1][2])
    if dp[i - 2][2] == len(c2):
        x2 = (dp[i - 2][0], dp[i - 2][1], dp[i - 2][2])
    else:
        x2 = (dp[i - 2][0] + c2[dp[i - 2][2]], dp[i - 2][1], dp[i - 2][2] + 1)
    if x1[0] > x2[0]:
        dp[i] = x1
    else:
        dp[i] = x2
ans = 0
cost3 = 0
for i in range(len(c3)):
    cost3 += c3[i - 1]
    cap = m - 3 * i
    if cap < 0:
        break
    ans = max(ans, cost3 + dp[cap][0])
print(ans)
