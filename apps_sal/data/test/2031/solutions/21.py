n = int(input())
A = list(map(int, input().split()))
L = A.copy()
L2 = L.copy()
A.sort()
c = int(input())
r = []
def S(x, L):
  idx = L.index(x)
  L[idx] = -1
  return [idx, x]
for i in range(c):
  k, pos = map(int, input().split())
  B = A[:0-k-1:-1]
  H = list(map(lambda x: S(x, L), B))
  H.sort()
  N = list(map(lambda x: x[1], H))
  r += [N[pos - 1]]
  L = L2.copy()
print('\n'.join(map(str, r)))
