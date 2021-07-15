t=int(input())
for i in range(t):
    z=list(map(int, input().split()))
    x=z[0]
    y=z[1]
    k=z[2]
    palok=k*y+k-1
    ans=0
    ans=palok//(x-1)
    if palok%(x-1)!=0:
        ans+=1
    print(ans+k)

