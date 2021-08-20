import numpy as np


def solve(N, Z, W, A):
    dp_x = np.full(N + 1, 1 << 61, dtype=np.int64)
    dp_y = np.zeros(N + 1, dtype=np.int64)
    for i in range(N - 1, 0, -1):
        dp_x[i] = max(dp_y[i + 1:].max(), abs(A[-1] - A[i - 1]))
        dp_y[i] = min(dp_x[i + 1:].min(), abs(A[-1] - A[i - 1]))
    ans = max(abs(A[-1] - W), dp_y[1:].max())
    return ans


(N, Z, W) = map(int, input().split())
A = np.array(input().split(), dtype=np.int64)
ans = solve(N, Z, W, A)
print(ans)
