for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=a[0]
    s=a[0]
    for i in range(1,n):
        s+=a[i]
        m=min(m,s)
    print(max(abs(m),0))
