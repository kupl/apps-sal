import numpy as np

N, K = map(int, input().split())
K2 = K*2

M = np.zeros((K2, K2), int)
nb = 0
for _ in range(N):
  x, y, c = input().split()
  x = int(x) % K2
  y = int(y) % K2
  if c=='B': nb+=1
  M[x, y] += 1 if c=='W' else -1

Sx = np.zeros((K2, K2+1), int)
for y in range(K2):
  Sx[:, y+1] = Sx[:, y] + M[:, y]

S = np.zeros((K2+1, K2+1), int)
for x in range(K2):
  S[x+1] = S[x] + Sx[x]

ans = -1000000
for x in range(K2):
  x0 = 0
  x1 = max(x-K , 0)
  x2 = x
  x3 = min(x+K , K2)
  x4 = K2

  T1 = S[x4] - S[x3] + S[x2] - S[x1]
  T2 = S[x3] - S[x2] + S[x1] - S[x0]

  U = T1[K2] - T1[K:K2] + T1[:K] + T2[K:K2] - T2[:K]
  ans = max(ans, np.max(U))
  
print(nb + ans)
