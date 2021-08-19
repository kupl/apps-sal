from sys import stdin, stdout
from math import gcd, ceil, sqrt
from collections import Counter


def ii1():
    return int(stdin.readline().strip())


def is1():
    return stdin.readline().strip()


def iia():
    return list(map(int, stdin.readline().strip().split()))


def isa():
    return stdin.readline().strip().split()


mod = 1000000007
(a, n, m) = iia()
rain = []
for _ in range(n):
    (l, r) = iia()
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
if umb[0][0] > rain[0]:
    print(-1)
else:
    print(dp[-1])
