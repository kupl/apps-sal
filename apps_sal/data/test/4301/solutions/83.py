N = int(input())
L = []
M = []
for i in range(N):
  a = int(input())
  L.append(a)
  M.append(a)
L.sort()
for j in range(N):
  if M[j] == L[len(L) - 1]:
    print(L[len(L) - 2])
  else:
    print(L[len(L) - 1])
