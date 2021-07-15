t=int(input())
for i in range(t):
    n=int(input())
    dig=0
    while 2**dig-1<n:
        dig+=1
    print(dig-1)
    D=dig-1
    num=1
    n-=1
    n-=D
    l=[0]*D
    for j in range(D):
        l[j]=min(num,n//(D-j))
        num+=l[j]
        n-=l[j]*(D-j)
    print(*l)
