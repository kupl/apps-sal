MOD = 2019
'\ndef part_count(S):\n  B = [0 for _ in range(MOD)]\n  C = [0 for _ in range(MOD)]\n  L = [0 for _ in range(MOD)]\n  R = [0 for _ in range(MOD)]\n  \n  if len(S) == 1:\n    s = S[0]\n    B[s] = 1 \n    return (B, L, R, C)\n  S_L = S[:len(S)//2]\n  S_R = S[len(S)//2:]\n  \n  B1, L1, R1, C1 = part_count(S_L)\n  B2, L2, R2, C2 = part_count(S_R)\n    \n  for j in range(MOD):\n    C[j] += C1[j] + C2[j]\n    L[j] += L1[j]\n    R[j] += R2[j]\n    for i in range(MOD):\n      B[j] += B1[i] * B2[(-i + j)%MOD]\n      L[j] += B1[i] * L2[(-i + j)%MOD]\n      R[j] += B2[i] * R1[(-i + j)%MOD]\n      C[j] += R1[i] * L2[(-i + j)%MOD]\n  \n  return (B, L, R, C) #両側隣接、左隣接、右隣接、隣接なしの個数\n'
S = list(input())
S.reverse()
N = len(S)
S = [int(S[i]) for i in range(N)]
MOD = 2019
a = 1
for i in range(N):
    S[i] *= a
    S[i] %= MOD
    a *= 10
    a %= MOD
T = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    T[i] += S[i - 1] + T[i - 1]
    T[i] %= MOD
C = [0 for i in range(MOD)]
for i in range(N + 1):
    C[T[i]] += 1
ans = 0
for i in range(MOD):
    ans += C[i] * (C[i] - 1) // 2
print(ans)
