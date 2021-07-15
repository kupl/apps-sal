from collections import defaultdict
from bisect import *

s,t = input(),input()
before,count = len(s),0
idx = defaultdict(list)

if not set(t) <= set(s):
  print("-1")
  return

for i,l in enumerate(s):
  idx[l] += [i]
  
for c in t:
  N = idx[c]
  index = bisect_left(N, before)
  if index > len(N) - 1:
    before = N[0] + 1
    count += 1
  else:
    before = N[index] + 1
    
print((count - 1) * len(s) + before)
