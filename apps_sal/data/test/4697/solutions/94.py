import sys

N, M=list(map(int,input().split()))
Mh=M//2

if N>Mh:
  print(Mh)
  return
else:
  rem=M-2*N
  print((rem//4+N))

