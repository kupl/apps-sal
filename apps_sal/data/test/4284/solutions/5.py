from sys import stdin
n=int(stdin.readline().strip())
for i in range(n):
    k,t,a,b=list(map(int,stdin.readline().strip().split()))
    low=0
    high=t
    while((high-low)>1):
        mid=(high+low)//2
        x=(t-mid)*b+(mid*a)
        if(x<k):
            low=mid
        else:
            high=mid

    x1=(t-high)*b+(high*a)
    x2=(t-low)*b+(low*a)
    if (x1<k):
        print(high)
    elif (x2<k):
        print(low)
    else:
        print(-1)
        
        

