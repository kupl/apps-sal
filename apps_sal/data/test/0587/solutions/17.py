n,k=map(int,input().split())
TD=[]
for i in range(n):
  t,d=map(int,input().split())
  TD.append([t,d])
TD.sort(key=lambda x:x[1],reverse=True)
V=set()
S=[]
ans=0
for t,d in TD[:k]:
  ans+=d
  if t in V:
    S.append(d)
  else:
    V.add(t)
ans+=len(V)**2
x=ans
for t,d in TD[k:]:
  if S==[]:
    break
  if not t in V:
    x=x-S.pop()+d-len(V)**2+(len(V)+1)**2
    V.add(t)
    ans=max(x,ans)
print(ans)
