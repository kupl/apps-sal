N=int(input())
S=input()
ans=0
cnt=0
for i in range(len(S)):
  if S[i]=='I':
    cnt+=1
  else:
    cnt-=1
  ans=max(ans,cnt)
print(ans)
