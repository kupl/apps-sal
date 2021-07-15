from itertools import *
N,A,B,C = map(int, input().split())
L = [int(input()) for n in range(N)]
ans = []

for i in product(range(4),repeat=N):
  a = 0
  b = 0
  c = 0
  d = 0
  for j in range(N):
    if i[j]:
      d+=1
      if i[j]==1:
        a+=L[j]
      elif i[j]==2:
        b+=L[j]
      else:
        c+=L[j]
  if a*b*c:
    ans+=[abs(A-a)+abs(B-b)+abs(C-c)+10*(d-3)]

print(min(ans))
