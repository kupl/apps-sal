N, K = map(int,input().split())
R, S, P = map(int,input().split())
T = input()
ans = 0
check = [0] * N
for i in range(N):
  j = T[i]
  if i >= K:
    if j == check[i-K]: continue
  if j == "r": ans += P
  elif j == "s": ans += R
  else: ans += S
  check[i] = j
 
print(ans)
