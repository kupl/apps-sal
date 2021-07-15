n, a, b = map(int, input().split())
if a+b-1 > n or a*b < n:
  print(-1)
  return
L = [[] for _ in range(b)]
L[-1] = list(range(1, a+1))
for now in range(a+1, n+1):
  temp = -2 - (now-(a+1))%(b-1)
  L[temp].append(now)
for l in L:
  print(*l, end=" ")
