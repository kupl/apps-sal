import numpy as np
import sys
input = sys.stdin.readline
read = sys.stdin.read
(n, t) = map(int, input().split())
m = map(int, read().split())
AB = sorted(zip(m, m))
(A, B) = zip(*AB)
dp = np.zeros((n + 1, t), dtype=np.int64)
for (i, (a, b)) in enumerate(AB):
    np.maximum(dp[i, a:], dp[i, :-a] + b, out=dp[i + 1, a:])
maxB = np.maximum.accumulate(B[::-1])[::-1]
ans = (dp[1:-1, -1] + maxB[1:]).max()
print(ans)
