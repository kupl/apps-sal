D,G=map(int,input().split())
pc=[list(map(int,input().split())) for i in range(D)]
ans=G // 100

for i in range(2**D):
    score=0
    b=0
    cnt=0
    for j in range(D):
        if ((i>>j)&1):
            score+=100*(j+1)*pc[j][0]+pc[j][1]
            cnt+=pc[j][0]
        else:
            b=j
    for k in range(pc[b][0]):
        if score>=G and cnt<ans:
            ans=cnt
        score+=(b+1)*100
        cnt+=1
print(ans)
