s=input();n=r=len(s)
for k in range(n-1):
  if s[k]!=s[k+1]:
    r=min(r,max(k+1,n-k-1))
print(r)
