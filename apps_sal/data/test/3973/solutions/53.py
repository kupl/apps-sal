import sys
input = sys.stdin.readline
from itertools import accumulate

n, m = map(int, input().split())
A = list(map(int, input().split()))
L = [0]*(2*m)
B = []
cnt = 0
for i in range(n-1):
  a, b = A[i], A[i+1]
  a -= 1
  b -= 1
  if a < b:
    cnt += b-a
    if b-a == 1:
      continue
    L[a+2] += 1
    L[b+1] += -1
    B.append((b+1, -(b-a-1)))
  else:
    b += m
    cnt += b-a
    if b-a == 1:
      continue
    L[a+2] += 1
    L[b+1] += -1
    B.append((b+1, -(b-a-1)))
L = list(accumulate(L))
for i, b in B:
  L[i] += b
L = list(accumulate(L))
c = 0
for i in range(m):
  c = max(c, L[i]+L[m+i])
ans = cnt - c
print(ans)
