for _ in range(int(input())):
    a,b,n=map(int,input().split())
    ans=0
    while a<=n and b<=n:
        if a>b:b+=a
        else:a+=b
        ans+=1
    print(ans)
