N,M=list(map(int,input().split()))
if 2*N>=M :
  print((M//2))
  return
print((N+(M-2*N)//4))

