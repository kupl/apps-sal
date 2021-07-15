n=int(input())
x=list(map(int,input().split()))
max_x=max(x)
min_x=min(x)
f=0
ans=1000000
for p in range(min_x,max_x+1):
    for i in range(n):
        f+=(x[i]-p)**2
    else:
        ans=min(ans,f)
        f=0
print(ans)
