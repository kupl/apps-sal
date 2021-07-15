for _ in range(int(input())):
    x,y,n=map(int,input().split())
    ans=(n//x)*x
    ans+=y
    if ans>n:
        ans-=x
    print(ans)    
