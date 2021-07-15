# 545 ms
from functools import lru_cache
n = int(input())
s = input()
A = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[j] + A[i - j] for j in range(0, i))

@lru_cache(None)
def score(s):
    length = len(s)
    if length == 0:
        return 0

    ans = 0
    start = 0
    i = 1
    while i < length and s[i] == s[start]:
        i += 1

    ans = dp[i] + score(s[i:])

    for j in range(i, length):
        if s[j] == s[start]:
            ans = max(ans, score(s[i:j]) + score(s[:i] + s[j:]))
    return ans


print(score(s))
