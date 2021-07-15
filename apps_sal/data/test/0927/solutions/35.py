def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    cost=[0,2,5,5,4,5,6,3,7,6]
    dp=[-n-n]*(n+1)
    dp[0]=0
    ans=[]
    for i in range(1,n+1):
        for j in a:
            if i>=cost[j]:
                dp[i]=max(dp[i],dp[i-cost[j]]+1)
    cnt=n
    while cnt:
        for j in a:
            if cnt>=cost[j] and dp[cnt-cost[j]]==dp[cnt]-1:
                ans.append(j)
                cnt-=cost[j]
                break
    for j in ans:
        print(j, end="")
    print("")

def __starting_point():
    main()
__starting_point()
