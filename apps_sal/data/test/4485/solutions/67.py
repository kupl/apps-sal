N, M = map(int, input().split())

A = set()
B = set()

for _ in range(M):
  a, b = map(int, input().split())
  if a == 1:
    A.add(b)
  if b == N:
    B.add(a)

if len(A&B):
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
