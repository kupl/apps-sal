N=int(input());

A,B=0,0;
for i in range(1,38):
  for j in range(1,26):
    if 3**i+5**j==N:
      A,B=i,j;
      break
    if A>0:
      break
      
if A>0:
  print(A,B);
else:
  print(-1)
