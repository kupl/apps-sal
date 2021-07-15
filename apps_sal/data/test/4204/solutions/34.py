s=input()
k=int(input())
ans=1
if len(s)==1:
  ans=s
else:
  for i in range(k):
    if s[i]!='1':
      ans=s[i]
      break
print(ans)
