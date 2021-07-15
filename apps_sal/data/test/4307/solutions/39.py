alist=[105,135,165,189,195]
ans=0
n=int(input())
for i in alist:
  if n>=i:
    ans+=1
print(ans)
