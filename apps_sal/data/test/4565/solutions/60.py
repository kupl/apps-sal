n=int(input())
s=list(input())

E=s.count('E')
W=s.count('W')

if s[0]=='E':
  ans=E-1
else:
  ans=E
  
ans1=[]
ans1.append(ans)
  
for x in range(1,n):
  if s[x]=='E':
    if s[x-1]=='E':
      ans-=1
      
  else:
    if s[x-1]=='W':
      ans+=1
  ans1.append(ans)
  
print(min(ans1))
