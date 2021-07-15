from collections import Counter

n=int(input())
INF = 10**20

d={}
for i in range(97,123):
  d[chr(i)] = INF

for i in range(n):
  s = input()
  c = Counter(s)
  for k in d.keys():
    if c.get(k):
      d[k] = min(c[k],d[k])
    else:
      d[k] = 0
    
keys=list(d.keys())
for k in keys:
  if d[k] == INF:
    del d[k]
    
ans = []
for k in d.keys():
  ans.extend([k]*d[k])
  
if len(ans)==0:
  print('')
  return
  
ans = sorted(ans)
print(''.join(ans))
