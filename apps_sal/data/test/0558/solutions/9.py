def __starting_point():
    M=998244353
    n,m,k=map(int,input().split())
    p,c=[m],[1]
    for i in range(1,n):
      p+=[p[-1]*(m-1)%M]
      c+=[c[-1]*(n-i)*pow(i,-1,M)%M]
    print(sum(p[n-i-1]*c[i] for i in range(k+1))%M)
__starting_point()
