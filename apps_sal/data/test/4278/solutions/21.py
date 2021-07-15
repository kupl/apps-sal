N = int(input())
D = {}
res = 0

for i in range(N):
  A = list(input())
  A.sort()
  if str(A) in D:
    res += D[str(A)]
    D[str(A)] += 1
  else:
    D[str(A)] = 1
    
print(res)
