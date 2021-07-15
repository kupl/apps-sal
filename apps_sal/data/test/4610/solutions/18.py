n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
from collections import Counter
ac=sorted(list(Counter(a).values()))
le=len(ac)
if le<=k:
  print((0))
else:
  count=0
  for i in range(le-k):
    count+=ac[i]
  print(count)

