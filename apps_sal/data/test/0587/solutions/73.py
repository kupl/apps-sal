import sys
input = sys.stdin.readline
from operator import itemgetter
import heapq
n, k = map(int, input().split())
TD = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True, key=itemgetter(1))
L = [[] for _ in range(n+1)]
P = []
a = 0
cnt = 0
F = [-float("inf")]*(n+1)
B = 0
for t, d in TD[:k]:
  if B>>t & 1:
    heapq.heappush(P, d)
  else:
    B |= 1 << t
    a += 1
  cnt += d
F[a] = cnt
for i in range(a, n):
  if len(P) == 0:
    break
  while k < n and B>>TD[k][0] & 1:
    k += 1
  if k == n:
    break
  t, d = TD[k]
  B |= 1 << t
  F[i+1] = F[i] - heapq.heappop(P) + d
ans = 0
for i in range(a, n+1):
  ans = max(ans, F[i] + i*i)
print(ans)
