n,m=map(int,input().split())
if n==m==1:
    print(1)
elif n==1 or m==1:
    if max(n,m)==2:
        print(0)
    else:
        print(max(n,m)-2)
else:
    print(n*m-(n*2+(m-2)*2))
