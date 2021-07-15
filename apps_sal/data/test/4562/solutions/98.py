N=int(input())
C=0
if N==1:
  print(1)
  return
for i in range(1,N):
  if i**2<N:
    C=i**2
  elif i**2==N:
    C=i**2
    break
  elif i**2>N:
    break
print(C)
