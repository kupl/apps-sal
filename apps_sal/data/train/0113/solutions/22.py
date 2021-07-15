for _ in range(int(input())):
    a,b=map(int,input().split())
    d=abs(a-b)
    ans=0
    sm=0 
    ans+=(d//5)
    d%=5 
    ans+=(d//2)
    d%=2 
    ans+=d 
    print(ans)
