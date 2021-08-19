import numpy as np
from sys import stdin
'\nReference: https://codeforces.com/blog/entry/75046#comment-591494 (1-based index)\n\n(0-based index)\n\nFor a sequence A[l]..A[k]..A[r] with sum S contributes l * (N - r) to answer.\n    0, 1, 2, ..., l....k....r, ..., N - 2, N - 1\n    x  x  x   x   x         v   v     v      v\nThere are l `x` and (N - r) `v`.\n\nEnumerate all possible sequence is impossible. \nConsider all sequeuces with sum S and **ends** at specific r:\n    A[l1]...A[r] -> l1 * (N - r)\n    A[l2]...A[r] -> l2 * (N - r)\n    A[l3]...A[r] -> l3 * (N - r)\n    .\n    .\n    .\nwhich contributes (l1 + l2 + ... + lm) * (N - r) in total.\n\nWe can find *sum of left index for all valid sequence* for each r using DP.\n\n    dp[i][s] = the sum of left index for all sequence that\n                    1. ends at i\n                    2. has sum s\n    \n    dp[i][:A[i]] = 0  since any sequence ends at i has sum >= A[i]\n\n    dp[i][A[i]] = i + 1\n    dp[i][s] = sum(dp[j][s - A[i]] for j in range(i))\n\n    Take A = [2, 3, 4] for example, sequences that end at A[2] are:\n    \n                   [4] -> dp[2][4] = 3\n             [2,    4] ↘\n                [3, 4] -> dp[2][s] = dp[2][s - 4] for all s\n             [2, 3, 4] ↗\n    \n    The answer is dp[r][S] * (N - r) for r in range(N)\n\nSo the naive implementation is:\n\n    dp = np.zeros((N, max(S, A.max()) + 1), dtype=np.int64)\n    for i, a in enumerate(A):\n        dp[i, a] = i + 1\n        for s in range(a + 1, S + 1):\n            dp[i, s] = dp[:i, s - a].sum() % M  # here can be optimized\n    \n    ans = 0\n    for i in range(N):\n        ans += (N - i) * dp[i, S]\n        ans = ans % M\n\nhas time O(N * S * N) which results in TLE.\n\nUsing another array to store the cumsum (prefix sum) of dp solves the problem:\n'
(N, S) = list(map(int, input().split()))
A = np.int32(input().split())
M = 998244353
V = max(A.max(), S)
ans = 0
dp = np.zeros((N, V + 1), dtype=np.int64)
cs = np.zeros(V + 1, dtype=np.int64)
for (i, a) in enumerate(A):
    dp[i, a] = i + 1
    dp[i, a + 1:S + 1] = cs[np.arange(a + 1, S + 1) - a]
    cs = (cs + dp[i]) % M
    ans = (ans + (N - i) * dp[i, S]) % M
print(ans)
