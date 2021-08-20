import numpy as np
(n, ma, mb) = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(n)]
dp = np.full((401, 401), 4001, int)
dp[0, 0] = 0
for (a, b, c) in abc:
    dp[a:, b:] = np.minimum(dp[a:, b:], dp[:-a, :-b] + c)
(ma_, mb_) = (ma, mb)
ans = 4001
while max(ma_, mb_) < 401:
    ans = min(ans, dp[ma_, mb_])
    ma_ += ma
    mb_ += mb
print(ans if ans < 4001 else -1)
