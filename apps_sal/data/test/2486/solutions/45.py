import numpy as np

N, K = list(map(int, input().split()))
A = tuple(map(int, input().split()))

dp_left = np.zeros((N + 1, K), dtype=bool)
dp_right = np.zeros((N + 1, K), dtype=bool)
dp_left[0, 0] = 1
dp_right[N, 0] = 1

for i in range(N):
    dp_left[i + 1] = dp_left[i]
    dp_right[N - i - 1] = dp_right[N - i]
    if (a := A[i]) < K:
        dp_left[i + 1, a:] |= dp_left[i, :-a]
    if (a := A[N - i - 1]) < K:
        dp_right[N - i - 1, a:] |= dp_right[N - i, :-a]

ans = 0
for i, a in enumerate(A):
    left_true = np.nonzero(dp_left[i])[0]
    right_true = np.nonzero(dp_right[i + 1])[0]

    ss = np.searchsorted(right_true, K - left_true) - 1
    if all(right_true[ss] + left_true + a < K):
        ans += 1

print(ans)
