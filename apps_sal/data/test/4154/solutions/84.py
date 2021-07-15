N, M = map(int, input().split())
res = 0
L_max = 0
R_min = 100000
for _ in range(M):
  L, R = map(int, input().split())
  if L_max < L: L_max = L
  if R < R_min: R_min = R
  
  
print(max(0, (R_min - L_max + 1)))
