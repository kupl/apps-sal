N=int(input())
CSF=[list(map(int,input().split())) for _ in range(N-1)]
for j in range(N):
    t=0
    for i in range(j,N-1):
        if t<CSF[i][1]:
            t=CSF[i][1]
        else:
            x=(t-1)//CSF[i][2]+1
            t=CSF[i][2]*x
        t+=CSF[i][0]
    print(t)

