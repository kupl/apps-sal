MOD = 2019
"""
def part_count(S):
  B = [0 for _ in range(MOD)]
  C = [0 for _ in range(MOD)]
  L = [0 for _ in range(MOD)]
  R = [0 for _ in range(MOD)]
  
  if len(S) == 1:
    s = S[0]
    B[s] = 1 
    return (B, L, R, C)
  S_L = S[:len(S)//2]
  S_R = S[len(S)//2:]
  
  B1, L1, R1, C1 = part_count(S_L)
  B2, L2, R2, C2 = part_count(S_R)
    
  for j in range(MOD):
    C[j] += C1[j] + C2[j]
    L[j] += L1[j]
    R[j] += R2[j]
    for i in range(MOD):
      B[j] += B1[i] * B2[(-i + j)%MOD]
      L[j] += B1[i] * L2[(-i + j)%MOD]
      R[j] += B2[i] * R1[(-i + j)%MOD]
      C[j] += R1[i] * L2[(-i + j)%MOD]
  
  return (B, L, R, C) #両側隣接、左隣接、右隣接、隣接なしの個数
"""

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

#B, L, R, C = part_count(S)
#print(B[0] + L[0] + R[0] + C[0])
T = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    T[i] += S[i - 1] + T[i - 1]
    T[i] %= MOD

# print(T)

C = [0 for i in range(MOD)]
for i in range(N + 1):
    C[T[i]] += 1

# print(C)

ans = 0
for i in range(MOD):
    ans += C[i] * (C[i] - 1) // 2

print(ans)
