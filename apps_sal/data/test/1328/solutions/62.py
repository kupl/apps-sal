import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n,ma,mb=MI()
    inf=10**9
    abc=[LI() for _ in range(n)]
    dp=[[[inf]*(n*10+1) for _ in range(10*n+1)] for _ in range(n+1)]
    dp[0][0][0]=0
    for i,(a,b,c) in enumerate(abc):
        for j in range(n*10+1):
            for k in range(n*10+1):
                pre=dp[i][j][k]
                if pre==inf:continue
                dp[i+1][j][k]=min(dp[i+1][j][k],pre)
                dp[i+1][j+a][k+b]=min(dp[i+1][j+a][k+b],pre+c)
    ans=inf
    for i in range(1,105):
        a=i*ma
        b=i*mb
        if a>n*10 or b>n*10:break
        ans=min(ans,dp[n][a][b])
    if ans==inf:print(-1)
    else:print(ans)

main()
