n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
x=list(t)
ans=0
for i in range(n):
  if x[i]=="r":x[i]="p"
  elif x[i]=="p":x[i]="s"
  else:x[i]="r"
for i in range(k):
  if x[i]=="r":ans+=r
  elif x[i]=="p":ans+=p
  else:ans+=s
for i in range(k,n):
  if x[i]==x[i-k]:
    x[i]="-"
    continue
  if x[i]=="r":ans+=r
  elif x[i]=="p":ans+=p
  else:ans+=s
print(ans)
