import numpy as np
(N, Q) = list(map(int, input().split()))
S = input()
s_l = np.zeros(N + 1)
for (i, s) in enumerate(S):
    if i + 1 < N and s == 'A' and (S[i + 1] == 'C'):
        s_l[i + 1] = s_l[i] + 1
    else:
        s_l[i + 1] = s_l[i]
for _ in range(Q):
    (l, r) = list(map(int, input().split()))
    print(int(s_l[r - 1] - s_l[l - 1]))
