n=int(input())
if n<=2:print(1);return
ng=0
ok=n
while ng+1!=ok:
  mid=(ng+ok)//2
  if mid*(mid+1)//2<=n+1:ng=mid
  else:ok=mid
print(n-ng+1)
