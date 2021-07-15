#author="_rabbit"
n=(int)(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=int(i)
if(sum%2==0):
    print(sum)
else:
    minn=int(1000000000000000)
    for i in a:
        if(i%2):
            minn=min(minn,i)
    sum=sum-minn
    print(sum)
    

