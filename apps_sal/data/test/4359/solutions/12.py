N = 5
A = [int(input()) for _ in range(N)]
 
if A[0] % 10 == 0 and A[1] % 10 == 0 and A[2] % 10 == 0 and A[3] % 10 == 0 and A[4] % 10 == 0:
  ans = sum(A)
else:
  ans = 0
  B = []
  for i in range(N):
    if A[i] % 10 == 0: ans += A[i]
    else: B.append(A[i])

  C = [k % 10 for k in B]
  m = C.index(min(C))
  for i in range(len(B)):
    if i == m: ans += B[i]
    else: ans += (B[i] // 10 + 1) * 10
  
print(ans)
