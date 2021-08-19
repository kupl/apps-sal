import numpy as np
I = [int(_) for _ in open(0).read().split()]
(N, T) = I[:2]
(A, B) = (I[2::2], I[3::2])
dp = np.array([-1] * 6001, dtype=np.int64)
dp[0] = 0
for (a, b) in sorted(zip(A, B)):
    dp_new = dp[:]
    dp_new[a:a + T] = np.maximum(dp[a:a + T], dp[:T] + b)
    dp = dp_new
print(max(dp))
