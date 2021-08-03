import numpy as np
N, M = (int(T) for T in input().split())
A = np.zeros((N, N), dtype=bool)
B = np.zeros((M, M), dtype=bool)
for TN in range(0, N):
    A[TN, :] = [True if T == '.' else False for T in input()]
for TM in range(0, M):
    B[TM, :] = [True if T == '.' else False for T in input()]
MatchFlag = False
for TR in range(0, N - M + 1):
    for TC in range(0, N - M + 1):
        if np.sum(A[TR:TR + M, TC:TC + M] ^ B) == 0:
            MatchFlag = True
print(['No', 'Yes'][MatchFlag])
