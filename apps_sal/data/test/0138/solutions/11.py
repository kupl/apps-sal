def solve():
    x=list(map(int,input().split()))
    remainder=x[0]%4
    if remainder==0:
        return 0;
    elif remainder==2:
        return min(2*x[1],x[2],2*x[3]);
    elif remainder==1:
        return min(3*x[1],x[1]+x[2],x[3]);
    else:
        return min(x[1],x[2]+x[3],x[3]*3);


print(solve())
    
    

