n, m = list(map(int, input().split()))
nn0 = n
nn1 = -1
mm0 = m
mm1 = -1
cnt = 0

for i in range(n):
  s = input().strip()
  if "B" in s:
    nn0 = min(i, nn0)
    nn1 = max(i, nn1)
    mm0 = min(s.index("B"), mm0)
    mm1 = max(s.rindex("B"), mm1)
    cnt += sum([z == "B" for z in s])
if nn1 < 0:
  print(1)
else:
  z = max(nn1-nn0, mm1-mm0) + 1  
  if z <= min(m,n):
    print(z*z - cnt)
  else:  
    print(-1)

