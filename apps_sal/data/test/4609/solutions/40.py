P = set()
N = int(input())
for i in range(N):
  A = int(input())
  if A in P:
    P.remove(A)
  else:
    P.add(A)
print(len(P))
