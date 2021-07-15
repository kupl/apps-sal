# N番目の竹をA,B,Cのいずれかに使うorどれにも使わないの全探索
# 4 ^ 8 = 60000強

import sys
readline = sys.stdin.readline

N,A,B,C = map(int,readline().split())
L = [int(readline()) for i in range(N)]

ans = 10 ** 10
import itertools
for prod in itertools.product(range(4),repeat = N):
  if len(set(prod) & set(range(3))) != 3:
    continue
  take = [0] * 3
  cost = 0
  for i in range(len(prod)):
    if prod[i] == 3:
      continue
    if take[prod[i]] != 0:
      cost += 10
    take[prod[i]] += L[i]
  cost += abs(A - take[0]) + abs(B - take[1]) + abs(C - take[2])
  if ans > cost:
    ans = cost

print(ans)
