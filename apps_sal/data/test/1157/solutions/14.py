import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
ans = [0, 0]
dp = [0, 0]
for i in arr:
    if i > 0:
        a = dp[0] + 1
        b = dp[1]
    else:
        a = dp[1]
        b = dp[0] + 1
    dp = [a, b]
    ans[0] += a
    ans[1] += b
    # print(dp)

print(*ans[::-1])
