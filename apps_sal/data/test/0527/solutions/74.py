import sys
readline = sys.stdin.readline

S = readline().rstrip()
T = readline().rstrip()

if len(set(T) - set(S)) > 0:
  print(-1)
  return
  
import bisect
# Tの各文字を探す
S2 = S * 2
from collections import defaultdict
# ある文字が何文字目にあるか辞書
dic = defaultdict(list)

for i in range(len(S2)):
  dic[S2[i]] += [i]

ind = -1
ans = 0
for t in T:
  # 探す文字はt
  targets = dic[t]
#  print("targets",targets,"t",t,"ind + 1",ind + 1)
  newind = targets[bisect.bisect_left(targets, ind + 1)]
#  print("t",t,"S2",S2,"newind",newind)
  ans += (newind - ind)
  if newind >= len(S):
    newind -= len(S)
  ind = newind

print(ans)
