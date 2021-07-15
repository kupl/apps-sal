"""T=int(input())
for _ in range(0,T):
    n=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""


T=int(input())
for _ in range(0,T):
    n,k=list(map(int,input().split()))
    ans=n
    if(n%2==0):
        ans+=(2*k)
    else:
        ans+=(2*(k-1))
        for i in range(2,n+1):
            if(n%i==0):
                ans+=i
                break
    print(ans)
    

