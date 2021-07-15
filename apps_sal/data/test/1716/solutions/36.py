N, M, Q = map(int, input().split())
S = [[0] * (N+1) for _ in range(N+1)]

for m in range(M):
  L, R = map(int, input().split())
  S[L][R] += 1
for l in range(1, N+1):
  for r in range(1, N+1):
    S[l][r] += S[l-1][r] + S[l][r-1] - S[l-1][r-1]

for i in range(Q):
  p, q = map(int, input().split())
  print(S[q][q] - S[p-1][q] - S[q][p-1] + S[p-1][p-1])
