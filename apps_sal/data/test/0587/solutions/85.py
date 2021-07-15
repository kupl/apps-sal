n,k=map(int,input().split())
INF=10**18
sushi=[[-INF] for _ in range(n)]
for _ in range(n):
  t,d=map(int,input().split())
  sushi[t-1].append(d)
for i in range(n):
  sushi[i].sort(reverse=True)
sushi.sort(key=lambda x:x[0],reverse=True)
q=[]
res=0
for i in range(k):
  res+=sushi[i][0]
  for j in sushi[i][1:]:
    q.append(j)
q.sort()
cur=res
res+=k**2
for var in range(1,k)[::-1]:
  a=q.pop()
  b=sushi[var][0]
  cur+=a-b
  res=max(res,cur+var**2)
print(res)
