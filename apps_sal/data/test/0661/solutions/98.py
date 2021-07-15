m,k=map(int,input().split())
if k<=2**m-1 and m>1:
    lists=[]
    for i in range(2**m-1,-1,-1):
        if i!=k:
            lists.append(i)
    lists.append(k)
    for i in range(2**m):
        if i!=k:
            lists.append(i)
    lists.append(k)
    print(*lists)
elif k<=2**m-1 and m==0:
    print(*[0,0])
    
elif k<=2**m-1 and m==1:
    if k==0:
        print(*[0,0,1,1])
    elif k==1:
        print(-1)

else:
    print(-1)
