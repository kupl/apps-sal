import bisect
def main():
    N,D,A=map(int,input().split())
    XH=[list(map(int,input().split())) for _ in range(N)]
    XH.sort()
    for i in range(N):
        XH[i][1]=-(-XH[i][1]//A)
    X=[x for x,a in XH]
    far=[0]*N
    for i in range(N):
        far[i]=bisect.bisect_right(X,X[i]+2*D)-1

    ans=0
    carry=0
    outrange=[0]*(N+1)
    for i in range(N):
        x=XH[i][0]
        hp=XH[i][1]
        carry-=outrange[i]
        if carry>=hp:
            continue
        outrange[bisect.bisect_right(X,X[i]+2*D)]+=hp-carry
        ans+=hp-carry
        carry+=hp-carry
    print(ans)

def __starting_point():
    main()
__starting_point()
