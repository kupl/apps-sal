l,r=map(int,input().split())
m=l//2019
l-=m*2019
r-=m*2019
if r>=2019:
    print(0)
    return
ans=2018
for i in range(l,r+1):
    for j in range(i+1,r+1):
        ans=min(ans,i*j%2019)
print(ans)
