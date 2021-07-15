n,t=input().strip().split(' ')
n,t=int(n),int(t)

arr=list(map(int,input().strip().split(' ')))
a=0
flag=1
while(flag and t):
    cnt=0
    x=t
    y=0
    flag=0
    for i in arr:
        if(x>=i):
            cnt+=1
            x-=i
            y+=i
            flag=1
    if(flag==0):
        break
    ans=t//y
    t-=y*ans
    cnt*=ans
    a+=cnt


print(a)


