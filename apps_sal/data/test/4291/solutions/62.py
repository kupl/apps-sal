N, Q = map(int, input().split())
S = input()
 
# 累積和的な発想
t = [0]*(N+1) # t[0]=t[1]=0
for i in range(N-1):
  t[i+2] = t[i+1]
  if S[i:i+2] == 'AC': t[i+2] += 1
    
for _ in range(Q):
  l,r = map(int, input().split())
  print(t[r] - t[l])
