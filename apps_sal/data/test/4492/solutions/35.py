N,x = map(int,input().split())
a = list(map(int, input().split()))
ans=0
wa=a[0]+a[1]
if wa>x:
    ans=wa-x
    if a[1]<ans:
        a[1]=0
    else:
        a[1]-=ans
for i in range(1,N-1):
    wa=a[i]+a[i+1]
    if wa>x:
        ans+=wa-x
        a[i+1]-=(wa-x)
print(ans)
