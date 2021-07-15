n,m = map(int,input().split())
al = []
kazu = []
for i in range(n):
  ka = list(map(str,input().split()))
  for j in range(int(ka[0])):
    al.append(ka[j+1])
from collections import Counter
l = Counter(al)
for i in range(m):
  kazu.append(l[str(i+1)])
print(kazu.count(n))
