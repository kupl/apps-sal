t=int(input())
for i in range (t):
    k=int(input())
    a=list(map(int,input().split()))
    wd=sum(a)
    rem=k%wd
    q=k//wd
    if(rem==0):
        rem=wd
        q=max(0,q-1)
    ma=10
    for i in range (7):
        ls=0
        for j in range (i,i+7):
            ls+=a[j%7]
            if(ls>=rem):
                ma=min(ma,j-i+1)
                break
    print(q*7+ma)
