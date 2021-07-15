n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
eat_bef=0
ans=0
for i in range(len(a)):
    ans+=b[a[i]-1]
    if i>=1:
        if eat_bef+1==a[i]:
            ans+=c[eat_bef-1]
    eat_bef=a[i]
print(ans)

