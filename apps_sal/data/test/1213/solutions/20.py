n,k=map(int,input().split())
los=input()
if n==1:
    print('PRINT',los,sep=' ')
else:
    if k>n/2 and k!=n and k!=1:
        for i in range(n-k):
            print('RIGHT')
        for i in range(n):
            print('PRINT',los[n-i-1],sep=' ')
            if i!=n-1:
                print('LEFT')
    if k<=n/2 and k!=n and k!=1:
        for i in range(k-1):
            print('LEFT')
        for i in range(n):
            print('PRINT',los[i],sep=' ')
            if i!=n-1:
                print('RIGHT')
    if k==1:
        for i in range(n):
            print('PRINT',los[i],sep=' ')
            if i!=n-1:
                print('RIGHT')
    if k==n:
        for i in range(n):
            print('PRINT',los[n-i-1],sep=' ')
            if i!=n-1:
                print('LEFT')


