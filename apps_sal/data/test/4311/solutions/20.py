s=int(input())
a=[]
ans=1
while True:
  a.append(s)
  if s%2==0:
    s//=2
  else:
    s=s*3+1
  ans+=1
  if s in a:
    print(ans)
    break
