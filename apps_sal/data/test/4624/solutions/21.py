for _ in range (int(input())):
    a,b=map(int,input().split())
    if(a<=2):
        print(1)
    else:
        a-=2
        ans=1
        if(a%b!=0):ans=2
        ans+=a//b
        print(ans)
