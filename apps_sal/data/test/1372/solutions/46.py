import numpy as np

H, N = list(map(int, input().split()))
A = []
B = []

for i in range(N):
  a, b = list(map(int, input().split()))
  A.append(a)
  B.append(b)
  
A = np.array(A)
B = np.array(B)
DP = np.zeros(H + 1)

for i in range(1, H + 1):
  DP[i] = np.amin(DP[np.maximum(i - A, 0)] + B)

print((int(DP[-1])))


