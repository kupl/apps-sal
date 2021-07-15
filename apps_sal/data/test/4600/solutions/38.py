N,M = map(int, input().split())
d = {'AC':0,'WA':0,}
b = 0
for i in range(N + 1):
  d[i] = 0
for j in range(M):
  p,s = input().split()
  p = int(p)
  if s == 'AC':
    if d[p] != -1:
      b = d[p]
      d[p] = -1
      d['AC'] += 1
      d['WA'] += b
      b = 0  
  if s == 'WA':
    if d[p] != -1:
       d[p] += 1
print(d['AC'],end = ' ')
print(d['WA'])
  


