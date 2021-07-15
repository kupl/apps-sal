N, Q = map(int, input().split())
S = input()
lr = [list(map(int, input().split())) for _ in range(Q)]

# 累積和
L = [0]*(N+1) # L[0]=L[1]=0
for i in range(N-1):
  L[i+2] = L[i+1]
  if S[i:i+2] == 'AC': L[i+2] += 1
    
for i in range(Q):
  l = lr[i][0]
  r = lr[i][1]
  print(L[r] - L[l])
