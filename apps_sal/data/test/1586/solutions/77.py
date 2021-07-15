n=int(input())
if n<2:
    print(0)
else:
    ans=0
    if n%2==1:
        print(0)
    else:
        ans+=n//10
        for i in range(100):
            ans+=n//(10*(5**(i+1)))
        print(ans)
