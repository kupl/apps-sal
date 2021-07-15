M,K = list(map(int, input().split()))

if 2 ** M <= K:
  print((-1))
  return
  
if M == 0:
  print((0,0))
elif M == 1 and K == 0:
  print((0,0,1,1))
elif M == 1 and K >= 1:
  print((-1))
else:
  A = list(range(2**M))
  B = A[:K] + A[K+1:]
  C = list(map(str, B + [K] + B[::-1] + [K]))
  print((" ".join(C)))
  

