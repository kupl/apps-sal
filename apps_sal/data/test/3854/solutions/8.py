from collections import Counter
import sys
n, k = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
dp = [0] * (k + 1)
dp[0] = 1
for i in c:
    tmp = dp[:]
    for j in range(k, i - 1, -1):
        tmp[j] |= dp[j - i] | (dp[j - i] << i)
    dp = tmp
b = bin(dp[-1])
ans = [i for i in range(k + 1) if b[-i - 1] == '1']
sys.stdout.write("{0}\n{1}".format(len(ans), str(ans)[1:-1].replace(",", "")))
