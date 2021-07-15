from collections import deque

n,m,s,t = list(map(int,input().split(' ')))
n += 1
a = list()
for i in range(n):
  a.append(None)
for i in range(n):
    a[i] = list()
for i in range(m):
  u,v = list(map(int,input().split(' ')))
  a[u].append(v)
  a[v].append(u)

resS = [n]*n
resT = [n]*n

resS[s] = 0
resT[t] = 0

q = deque() #очередь

q.append(s)
while len(q)!=0:
  w = q.popleft()
  for i in a[w]:
    if resS[i] <= resS[w]:
        continue
    q.append(i)
    resS[i] = resS[w] + 1
     

q.append(t)
while len(q)!=0:
  w = q.popleft()
  for i in a[w]:
    if resT[i] <= resT[w]:
        continue
    q.append(i)
    resT[i] = resT[w] + 1

res = 0 
for i in range(1,n-1):
  for j in range(i+1,n):
    if not(j in a[i]) and resS[i]+resT[j]+1>=resS[t] and resT[i]+resS[j]+1>=resS[t]:
      res += 1

print(res)
