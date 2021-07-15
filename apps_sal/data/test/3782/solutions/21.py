import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
A = list(map(int, input().split())) + [-1]
ans = float("inf")
for a in A:
  L = []
  K = []
  for t in A:
    if t >= a:
      L.append(t)
    else:
      L.sort()
      for c in range(len(L)-k+1):
        K.append(L[c])
      L = []
  K.sort()
  if len(K) < q:
    continue
  else:
    y = K[q-1]
    ans = min(ans, y-a)
print(ans)
