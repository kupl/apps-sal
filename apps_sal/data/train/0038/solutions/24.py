for i in ' '*int(input()):
    n,k1,k2=map(int,input().split())
    L1=list(map(int,input().split()))
    L2=list(map(int,input().split()))
    if max(L1)>max(L2):print('YES')
    else:print('NO')
