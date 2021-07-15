D,G=list(map(int,input().split()))
s=[list(map(int,input().split())) for _ in range(D)]

ans=10000
for i in range(2**D):
    score=0
    cnt=0
    rest=[]
    for j in range(D):
        if (i>>j)&1:
            score+=100*(j+1)*s[j][0]+s[j][1]
            cnt+=s[j][0]
        else:
            rest.append(j)

    if score<G:
        r=rest[-1]
        for _ in range(s[r][0]-1):
            score+=100*(r+1)
            cnt+=1
            if score>=G: break

    if score>=G:
        ans=min(cnt,ans)

print(ans)

