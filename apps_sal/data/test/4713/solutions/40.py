n=int(input())
s=input()
ans=0
x=0
for i in range(n):
  if s[i]=='I':
    x+=1
  else:
    x-=1
  ans=max(ans,x)
print(ans)
