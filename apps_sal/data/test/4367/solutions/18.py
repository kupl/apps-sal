n,r=map(int,input().split())
if n<10:
  ans=r+(100*(10-n))
else:
  ans=r
print(ans)
