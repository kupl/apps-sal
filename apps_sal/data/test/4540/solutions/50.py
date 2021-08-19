import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
A = np.append(A, 0)
A = np.insert(A, 0, 0)
S = sum(abs(np.diff(A[:])))
for i in range(1, len(A) - 1):
    if A[i - 1] == A[i]:
        print(S)
    elif A[i - 1] < A[i] and A[i] < A[i + 1] or (A[i - 1] > A[i] and A[i] > A[i + 1]):
        print(S)
    else:
        print(S - min(abs(A[i - 1] - A[i]), abs(A[i] - A[i + 1])) * 2)
