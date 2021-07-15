n=int(input().strip())
a=list(map(int, input().split()))
su=0
ans1=0
ans2=0
for i in range(n):
    if i%2==0:
        su+=a[i]
        if su<=0:
            ans1+=abs(su-1)
            su=1
    if i%2==1:
        su+=a[i]
        if su>=0:
            ans1+=abs(su+1)
            su=-1
su=0
for i in range(n):
    if i%2==0:
        su+=a[i]
        if su>=0:
            ans2+=abs(su+1)
            su=-1
    if i%2==1:
        su+=a[i]
        if su<=0:
            ans2+=abs(su-1)
            su=1

print(min(ans1,ans2))
