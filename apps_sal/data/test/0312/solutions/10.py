n,m=[int(x) for x in input().split()]
if n==1:
    print(1)
elif n&1:
    if m>n//2:
        print(m-1)
    else:
        print(m+1)
else:
    if m<=n/2:
        print(m+1)
    else:
        print(m-1)
    

