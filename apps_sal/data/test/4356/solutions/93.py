import numpy as np

N, M = map(int, input().split())
A = np.array([list(str(input())) for i in range(N)])
B = np.array([list(str(input())) for j in range(M)])
ans = "No"

for i in range(N - M + 1):
    for j in range(N - M + 1):
        x = [s[j:M + j] for s in A[i:M + i]]
        if np.count_nonzero((x == B) == 0) == 0:
            ans = "Yes"

print(ans)
