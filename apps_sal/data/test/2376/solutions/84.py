import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n, lim = MI()
    ww = []
    vv = []
    for _ in range(n):
        w, v = MI()
        ww.append(w)
        vv.append(v)
    w0=ww[0]
    # dp[i][j]…荷物の個数がiで、端数の合計がjのときの価値の最大値
    dp=[[0]*(3*n+1) for _ in range(n+1)]
    for w,v in zip(ww,vv):
        for i in range(n,0,-1):
            sj=min(lim-i*w0,3*n)
            for j in range(sj,-1,-1):
                nj=j-(w-w0)
                if nj<0:break
                dp[i][j]=max(dp[i][j],dp[i-1][nj]+v)
    #p2D(dp)
    print(max(max(row) for row in dp))

main()

