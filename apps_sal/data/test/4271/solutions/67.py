n=int(input());ans=0
a=[*map(int,input().split())]
b={i+1:j for i,j in enumerate(map(int,input().split()))}
c={i+1:j for i,j in enumerate(map(int,input().split()))}
ans+=b[a[0]]
for i in range(1,n):
  if a[i]-(a[i-1])==1:
    ans+=c[a[i-1]]
  ans+=b[a[i]]
print(ans)
