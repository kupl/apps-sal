d,n=map(int,input().split())
if d==0:
    if n!=100:
        print(n)
    else:
        print(101)
else:
    a=[n]+[0]*(2**d)
    if n!=10**2:
        print(*a,sep="")
    else:
        a[-(2*d+1)]+=1
        print(*a,sep="")
