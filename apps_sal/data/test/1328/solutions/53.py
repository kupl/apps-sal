N,A,B = map(int,input().split())
X = [1<<20]*4040

for n in range(N):
  a,b,c = map(int,input().split())
  t = A*b-B*a
  X = [min(X[m],(0 if (m-t)%4040==0 else X[(m-t)%4040])+c) for m in range(4040)]

if 1<<18<X[0]:
  print(-1)
else:
  print(X[0])
