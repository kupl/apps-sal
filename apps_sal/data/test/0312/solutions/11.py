n,m=list(map(int,input().split(' ')))
if n==1:
    print(1)
else:
    if n%2==0:
        if m<=n//2:
            print(m+1)
        else:
            print(m-1)
    else:
        if m<=(n-1)//2:
            print(m+1)
        else:
            print(m-1)
