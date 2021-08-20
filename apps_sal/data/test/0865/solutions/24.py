import numpy as np
(n, t) = map(int, input().split())
DP = np.full(t, -float('inf'))
DP[0] = 0
ans = 0
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
for (a, b) in ab:
    ans = max(ans, max(DP) + b)
    if a < t:
        DP[a:] = np.maximum(DP[a:], DP[:-a] + b)
ans = int(ans)
print(ans)
