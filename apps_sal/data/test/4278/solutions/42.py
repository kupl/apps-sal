n=int(input())
l=[]

for i in range(n):
  l.append(sorted(input()))

l.sort()

clst=[]
cnt=0
for i in range(len(l)-1):
  if l[i]==l[i+1]:
    cnt+=1
    if i == len(l)-2:
      clst.append(cnt)
  else:
    if cnt > 0:
      clst.append(cnt)
    cnt=0

ans=0
for x in clst:
  ans+=(1+x)*x//2 
print(ans)
