def main():
    N,K = map(int,input().split())
    XY = [list(map(int,input().split())) for _ in [0]*N]
    
    iX = sorted(x for x,y in XY)
    iY = sorted(y for x,y in XY)
    X = {x:i for i,x in enumerate(iX)}
    Y = {y:i for i,y in enumerate(iY)}

    c = [[0]*(N+1) for i in [0]*(N+1)]
    for x,y in XY:
        c[Y[y]+1][X[x]+1] = 1

    for i in range(N):
        ci1 = c[i+1]
        for j in range(N):
            ci1[j+1] += ci1[j]
    for i in range(N):
        ci1 = c[i+1]
        ci = c[i]
        for j in range(N):
            ci1[j+1] += ci[j+1]

    ans = 10**20
    for u in range(N):
        for d in range(u+K-1,N):
            l = 0
            r = 1
            dY = iY[d]-iY[u]
            cd = c[d+1]
            cu = c[u]
            while r<N:
                if cd[r+1]+cu[l]-cu[r+1]-cd[l] >=K:
                    ans = min(ans, (iX[r] - iX[l])*dY)
                    l+=1
                else:r+=1

    print(ans)
main()
