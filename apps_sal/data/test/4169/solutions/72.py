n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()
ans=0
for i in range(n):
    if m>ab[i][1]:
        ans+=ab[i][0]*ab[i][1]
        m-=ab[i][1]
    else:
        ans+=ab[i][0]*m
        print(ans)
        break
