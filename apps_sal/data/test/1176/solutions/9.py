n=int(input())
a=list(map(int,input().split()))

cnt=0
ans=0

for i in range(n):
    if a[i]<0:
        cnt+=1
        a[i]*=-1



if cnt%2==0:
    ans=sum(a)

else:
    ans=sum(a)-2*min(a)

print(ans)

