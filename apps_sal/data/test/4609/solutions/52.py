n=int(input())
a={}
for i in range(n):
  a_=int(input())
  if a_ not in a:
    a[a_]=1
  else:
    a[a_]+=1
ans=0
for i in a:
  if a[i]%2==1:
    ans+=1
print(ans)
