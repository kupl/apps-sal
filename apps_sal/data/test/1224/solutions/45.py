N=int(input())
A,B=0,0
for i in range(1,41):
  for j in range(1,31):
    if 3**i+5**j==N:
      A,B=i,j
if A==0 and B==0:
  print(-1)
else:
  print(A,B)
