n=int(input())
f=[list(map(int,input().split())) for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
maxp=-float("inf")
for i in range(1,2**10):
  pt=0
  for j in range(n):
    cnt=0
    for k in range(10):
      if (i>>k)&1 and f[j][k]==1:
        cnt+=1
    pt+=p[j][cnt]
  maxp=max(maxp,pt)
print(maxp)
