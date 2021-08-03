import numpy as np
n, m = map(int, input().split())
A = np.array([list(input()) for i in range(n)])
B = np.array([list(input()) for j in range(m)])
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if np.all(B == A[i:i + m, j:j + m]):
            print("Yes")
            return
print("No")
