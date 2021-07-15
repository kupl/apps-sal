N, M = [int(x) for x in input().split()]
L = list()
R = list()
for i in range(M):
  l, r = [float(x) for x in input().split()]
  L.append(l)
  R.append(r)
Lmax = max(L)
Rmin = min(R)
if(Rmin-Lmax)<0:
  print(0)
else:
  print(int(Rmin-Lmax+1))
