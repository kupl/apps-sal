t=int(input())
while t>0 :
    n=int(input())
    l=list(map(int,input().split()))
    f=0 
    for i in range(1,n) :
        if l[i]>=l[i-1] :
            f=1 
            break
    if (f==0) :
        print("NO")
    else :
        print("YES")
    t-=1
