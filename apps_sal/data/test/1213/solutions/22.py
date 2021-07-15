n,k=list(map(int,input().split()))
s=input().strip()
if n-k<k-1:
    for i in range(n-k):
        print('RIGHT')
    for i in reversed(list(range(1,n))):
        print('PRINT',s[i])
        print('LEFT')
    print('PRINT',s[0])
else:
    for i in range(k-1):
        print('LEFT')
    for i in range(n-1):
        print('PRINT',s[i])
        print('RIGHT')
    print('PRINT',s[n-1])

