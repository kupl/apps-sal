n,A,B=map(int,input().split())
hole=[*enumerate(map(int,input().split()))]
si=hole[0][1]
hole.sort(reverse=True,key=lambda x:x[1])
s=0
ans=0
for n,i in hole: s+=i
for n,i in hole:
  if (si*A)//s>=B: break
  if n==0: continue
  s-=i
  ans+=1

print(ans)
