for _ in range(int(input())):
    n,r=map(int,input().split())
    if r>n:
        r=n
    ans=0
    if r==n:
        ans+=1
        r=n-1
    print(ans+((r*(r+1))//2))
