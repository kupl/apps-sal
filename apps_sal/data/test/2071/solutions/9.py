import sys
import io

stream_enable = 0

inpstream = """
3
1 2 3
6 5 4
"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


n = int(input())
arr = [inpmap(), inpmap()]

s = [0] * n
s[-1] = arr[0][-1] + arr[1][-1]
for i in range(n - 2, -1, -1):
    s[i] = s[i + 1] + arr[0][i] + arr[1][i]

a = [0] * n
a[-1] = arr[1][-1] * 2 + arr[0][-1]
b = [0] * n
b[-1] = arr[0][-1] * 2 + arr[1][-1]
for i in range(n - 2, -1, -1):
    a[i] = arr[0][i] + a[i + 1] + s[i + 1] + arr[1][i] * (n - i) * 2
    b[i] = arr[1][i] + b[i + 1] + s[i + 1] + arr[0][i] * (n - i) * 2

dp = [0] * n
dp[-1] = arr[n % 2][-1]
for i in range(n - 2, -1, -1):
    d = i % 2
    g1 = arr[1 - d][i] + dp[i + 1] + s[i + 1] * 2
    g2 = (a, b)[d][i + 1] + arr[1 - d][i] * ((n - i) * 2 - 1)
    dp[i] = max(g1, g2)
print(dp[0])
