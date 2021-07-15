for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    ans=0
    while(n>0):
        if(n%k==0):
            n//=k
            ans+=1
        else:
            ans+=n%k
            n-=n%k
    print(ans)

