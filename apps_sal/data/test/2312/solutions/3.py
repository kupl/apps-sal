t=int(input())
while t>0 :
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    l.sort()
    for i in range(1,n) :
        if (l[i]==l[i-1]) :
            f=1 
            break
    if f==1 :
        print("YES")
    else :
        print("NO")
    t-=1
