n,m,x = map(int,input().split())
cost = []
cont = []
for i in range(n):
  c,*a = map(int,input().split())
  cost.append(c)
  cont.append(a)

ans = 10**9
for bit in range(1<<n):
  cnt = 0
  skills = [0]*m
  for i in range(n):
    if (bit>>i) & 1:
      cnt += cost[i]
      for j,pts in enumerate(cont[i]):
        skills[j] += pts
  if min(skills)>=x:
    ans = min(ans, cnt)
print(ans if ans<10**9 else -1)
