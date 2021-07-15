S=input()
agct='AGCT'
ans=0
s=0
for i in range(len(S)):
  cnt=0
  if S[i] in agct:
    j=0
    while i+j<len(S) and S[i+j] in agct:
      cnt+=1
      j+=1
    ans=max(ans,cnt)
print(ans)
