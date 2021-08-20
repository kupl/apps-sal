import numpy as np
(N, S) = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
P = 998244353
table = np.zeros((N, S + 1), dtype=int)
table[0, 0] = 2
if A[0] <= S:
    table[0, A[0]] = 1
for i in range(1, N):
    Ai = A[i]
    table[i] += 2 * table[i - 1]
    if Ai <= S:
        table[i][Ai:] += table[i - 1][:S - Ai + 1]
    table[i] = table[i] % P
print(table[N - 1][S])
