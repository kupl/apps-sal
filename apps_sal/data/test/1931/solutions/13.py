import sys


def input():
    return sys.stdin.readline().strip()


ipnut = input
dp = [0]
n = 0
while dp[-1] < 1000000000:
    n += 1
    dp.append(n * (3 * n + 1) // 2)
for i in range(int(input())):
    n = int(input())
    k = 0
    while n > 1:
        k += 1
        l = 0
        r = len(dp)
        while r - l > 1:
            m = (r + l) // 2
            if dp[m] <= n:
                l = m
            else:
                r = m
        n -= dp[l]
    print(k)
'\n10\n10 11 12 13 14 15 16 17 11 11\n'
