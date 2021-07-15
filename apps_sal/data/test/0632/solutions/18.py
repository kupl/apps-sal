for i in range(int(input())):
    n,k=map(int,input().split())
    ind=-1
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            ind=j
            break
    if ind==-1:
        ind=n
    k-=1
    su=n+ind+(k)*2
    print(su)
