S=input()
l=len(S)

import itertools as it
a=0
for i in range(l):
 for j in it.combinations(range(1,l), i):
  t='';p=0
  for k in j:
    t+=S[p:k]+'+'
    p=k
  t+=S[p:]
  a+=eval(''.join(t))
print(a)
