n,c = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(c)]

a = [[0]*c for _ in range(3)]
b = [[[0,i] for i in range(c)] for _ in range(3)]

for i in range(n):
  l = list(map(int,input().split()))
  for j in range(n):
    a[(i+j)%3][l[j]-1] += 1
    
for i in range(3):
  for k in range(c):
    b[i][k][0] = sum([a[i][t]*d[t][k] for t in range(c)])
p = [[],[],[]]
for i in range(3):
  p[i] = sorted(b[i])[:3]
m = []
for t in p[0]:
  for s in p[1]:
    for u in p[2]:
      if (t[1] != s[1]) and (t[1] != u[1]) and (s[1] != u[1]):
        m.append(t[0]+s[0]+u[0])
print(min(m))
