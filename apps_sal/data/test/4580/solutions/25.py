N = int(input())
A = list(map(int,input().split()))
L = []
H = []

for i in range(N):
  a = A[i]//400
  if a > 7:
    H.append(a)
  else:
    L.append(a)

if len(L) != 0:
  print(str(len(set(L)))+" "+str(len(set(L))+len(H)))
else:
  print("1 "+str(len(H)))
