# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 03/07/2020

from sys import stdin, stdout
from math import gcd, ceil, sqrt
from collections import Counter
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
mod = 1000000007

a, n, m = iia()
rain = []
for _ in range(n):
    l, r = iia()
    for i in range(l, r):
        rain.append(i)
umb = []
for _ in range(m):
    umb.append(iia())

rain.sort()
umb.sort()

dp = [0] * (a + 1)
for i in range(a + 1):
    if i not in rain:
        if i != 0:
            dp[i] = dp[i - 1]

    else:
        for j in umb:
            if j[0] <= i:
                temp = (i + 1 - j[0]) * j[1]

                if j[0] - 1 >= 0:
                    temp += dp[j[0] - 1]

                if dp[i] > 0:
                    dp[i] = min(dp[i], temp)

                else:
                    dp[i] = temp

            else:
                break

# print(dp)

if umb[0][0] > rain[0]:
    print(-1)
else:
    print(dp[-1])
