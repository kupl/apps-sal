N, M = map(int, input().split())
L = 1
R = N
for i in range(M):
  l, r = map(int, input().split())
  if L < l:
    L = l
  if R > r:
    R = r
  if R < L:
    print(0)
    break
else:
  print(R - L + 1)
