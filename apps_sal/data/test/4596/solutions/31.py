N = int(input())
A = list(map(int, input().split()))

i = 1
escape = False
while 1:
  for j in range(N):
    if A[j] % (2 ** i) == 0:
      pass
    else:
      escape = True
      break
  else:
    i += 1
  
  if escape:
    break
    
print((i - 1))

