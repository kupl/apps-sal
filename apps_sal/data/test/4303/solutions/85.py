import bisect
import math
(N, K) = map(int, input().split())
X = list(map(int, input().split()))
a = bisect.bisect_left(X, 0)
X.insert(a, 0)
ans = math.inf
for i in range(max(0, a + K - N), min(a + 1, K + 1)):
    ans = min(ans, -X[a - i] * 2 + X[a + K - i], -X[a - i] + X[a + K - i] * 2)
print(ans)
