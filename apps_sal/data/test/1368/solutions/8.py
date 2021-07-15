from collections import Counter
n,a,b=list(map(int,input().split()))
v=list(map(int,input().split()))
v.sort(reverse=True)
su=sum(v[:a])
avg=su/a
tot=0
inside=0
c=[ [0]*51 for _ in range(51)]
for i in range(n+1):
    for j in range(i+1):
        if j==0 or j==i:
            c[i][j]=1
        else:
            c[i][j]=c[i-1][j]+c[i-1][j-1]
for i in range(n):
    if v[i]==v[a-1]:
        tot+=1
        if i<a:
            inside+=1
cnt=0
if inside==a:
    for i in range(a,b+1):
        cnt+=c[tot][i]
else:
    cnt+=c[tot][inside]
print(avg)
print(cnt)

        



