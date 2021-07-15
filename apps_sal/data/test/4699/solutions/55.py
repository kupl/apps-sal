N, K = map(int,input().split())
mat = input().split()
while True:
  FIN = 0
  for i in range(len(str(N))):
    for j in range(K):
      if mat[j] == str(N)[i]:
        FIN += 1
        break
  if FIN == 0:
    break 
  else:
    N += 1
print(N)
