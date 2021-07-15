n,m,c=map(int,input().split())
B=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(n)]
ans=0
for a in A:
  s=c
  for i in range(m):
    s += a[i]*B[i]
  if s>0:
    ans += 1
print(ans)
