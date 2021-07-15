n,m=map(int,input().split())
s=input()[::-1]
ans=[]
now=0
while(now<n):
  t=1
  for i in reversed(range(1,m+1)):
    if now+i>n or s[now+i]=='1':
        continue
    now=now+i
    ans.append(i)
    t=0
    break
  if t:
    print(-1)
    return
ans.reverse()
print(*ans,sep=' ')
