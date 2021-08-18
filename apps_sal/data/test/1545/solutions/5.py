
import sys
mod = pow(10, 9) + 7

n = int(sys.stdin.readline())
s = sys.stdin.readline()[:-1]
a = [int(x) for x in sys.stdin.readline().split()]

dp = [0 for _ in range(n + 1)]
dp[0] = 1


def ci(c):
    return ord(c) - ord('a')


l = 0
for i in range(1, n + 1):
    f = 0
    for x in range(i - 1, -1, -1):
        f = max(f, i - a[ci(s[x])])
        if f > x:
            continue
        dp[i] = (dp[i] + dp[x]) % mod
        l = max(l, i - x)

print(dp[n])
print(l)

res = 1
m = 9999
j = 0
for i in range(n):
    m = min([a[ci(s[x])] for x in range(j, i + 1)])
    if m < i - j + 1:
        res += 1
        j = i
print(res)
