# Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open('input.txt', 'r')
MOD = 998244353
sys.setrecursionlimit(1000000)


def check(i):
    if not dp[i][2]:
        return False
    if i < 0:
        return True
    return check(i - dp[i][1])


n, k, d = map(int, input().split())
if k == 1:
    print('YES')
    return
a = sorted(map(int, input().split()))
dp = [None for i in range(n)]
dp[0] = (a[0], 1, False)
for i in range(1, n):
    if a[i] - dp[i - 1][0] <= d:
        dp[i] = (dp[i - 1][0], dp[i - 1][1] + 1, dp[i - 1][1] + 1 >= k)
    else:
        dp[i] = (a[i], 1, False)
        j = i
        while a[i] - a[j] <= d and j > 0:
            j -= 1
            if dp[j][2]:
                dp[i] = (a[j + 1], i - j, i - j >= k)
            if dp[i][2]:
                break
print('YES' if check(n - 1) else 'NO')
