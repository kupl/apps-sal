n,m=list(map(int,input().split()))
l_n=[list(map(int,input().split())) for _ in range(n)]
l_m=[list(map(int,input().split())) for _ in range(m)]
# print(l_n,l_m)


for i,j in l_n:
    distance=0
    cnt = 0
    ans = float ( "inf" )
    for k,l in enumerate(l_m,1):
        a,b=l
        distance=abs(i-a)+abs(j-b)
        if ans>distance:
            ans=min(ans,distance)
            cnt=k
    print(cnt)

