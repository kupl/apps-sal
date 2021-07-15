N, A, B, C = map(int, input().split())
from itertools import product
l = [int(input()) for i in range(N)]
ans = []
for i in product(range(4), repeat=N):
  a = 0
  b = 0
  c = 0
  d = 0
  for j in range(N):
    if i[j]:
      d += 1
      if i[j] == 1:
        a += l[j]
      elif i[j] == 2:
        b += l[j]
      else:
        c += l[j]
  if a * b * c:
    ans += [abs(A - a) + abs(B - b) + abs(C - c) + (d - 3) * 10]
print(min(ans))
