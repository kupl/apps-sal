import math
import sys
N = int(input())
P = list(map(float, input().split()))

P = sorted(P, reverse=True)
if 1.0 in P:
  print(1.0)
  return
def solve(P_):
  log_prod_all = 0
  for p in P_:
    log_prod_all += math.log(1-p)
  return sum([math.exp(math.log(p)-math.log(1-p)+log_prod_all) for p in P_])
print(max([solve(P[:i]) for i in range(len(P)+1)]))
