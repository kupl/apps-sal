n=int(input())
s=input()
data=[]
ans=0
for i in range(n-1):
  if s[i] not in data:
    data.append(s[i])
  res=0
  for j in data:
    if j in s[i+1:n]:
      res+=1
  ans=max(ans,res)
print(ans)
