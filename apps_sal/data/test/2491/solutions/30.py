import sys
rl=sys.stdin.readline

def main():
    n,m=list(map(int,rl().strip().split()))
    eaw=[list(map(int,rl().strip().split())) for _ in range(m)]
    d=dict(((x[0]-1,x[1]-1),-x[2]) for x in eaw)
    inf=10**14
    mdl=[inf]*n
    mdl[0]=0
    def blrelax(dl,k):
        for _ in range(k):
            for e in iter(d):
                if dl[e[0]]+d[e]<dl[e[1]]:
                    dl[e[1]]=dl[e[0]]+d[e]
    blrelax(mdl,n-1)
    a1=mdl[n-1]
    blrelax(mdl,n)
    a2=mdl[n-1]
    if a1>a2:
        print('inf')
    else:
        print((-a1))
    
def __starting_point():
    main()

__starting_point()
