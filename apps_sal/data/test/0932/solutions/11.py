m,n = list(map(int,input().split()))
B = [list(map(int,input().split())) for i in range(m)]
sr = [sum(B[i]) for i in range(m)]
sc = [sum([B[i][j] for i in range(m)]) for j in range(n)]
no = sum(sr) > 0 and (max(sr) < n or max(sc) < m)

for i in range(m):
  for j in range(n):
    if B[i][j] and sc[j]%m and sr[i]%n or no:
      print('NO')
      return

print('YES')
for i in range(m):
  Ai = [(sr[i]//n)*(sc[j]//m) for j in range(n)]
  print(' '.join(repr(a) for a in Ai))

