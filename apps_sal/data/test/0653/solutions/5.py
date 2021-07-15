n=int(input())
s=input()
ans=[0]*10
for i in range(n):
  if s[i]=='L':
    for j in range(10):
      if ans[j]==0:
        ans[j]=1
        break
  elif s[i]=='R':
    for j in range(9,-1,-1):
      if ans[j]==0:
        ans[j]=1
        break
  else:
    ans[int(s[i])]=0
print(''.join(map(str,ans)))
