import numpy as np
N = int(input())
S = np.array([int(x) for x in input().split()], dtype=np.int64)
answer = 0
for d in range(1, N):
    cum_left = np.cumsum(S[::d])
    cum_right = np.cumsum(S[::-1][::d])
    score = cum_left + cum_right
    for (L, s) in enumerate(score):
        if answer >= s:
            continue
        A = N - 1 - L * d
        B = A - d
        if A <= 0:
            continue
        if A <= B:
            continue
        if B <= 0:
            continue
        if (N - 1) % d == 0 and 2 * L * d >= N - 1:
            continue
        answer = s
print(answer)
