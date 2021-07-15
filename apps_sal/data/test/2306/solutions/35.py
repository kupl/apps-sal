import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n=int(input())
    tt=LI()
    vv=LI()+[0]
    #区間の変わり目においてのvの最大値を左右から調べる
    y=0
    max_vL=[1000]*(n-1)
    max_vR=[1000]*(n-1)
    for i in range(n-1):
        y=min(vv[i],vv[i+1],y+tt[i])
        max_vL[i]=y
    y=0
    for i in range(n-2,-1,-1):
        y=min(vv[i+1],vv[i],y+tt[i+1])
        max_vR[i]=y
    #print(max_vR)
    #print(max_vL)
    #左右のminを取ることで、変わり目のvを決める
    yy=[0]*(n+1)
    for i in range(n-1):
        yy[i+1]=min(max_vL[i],max_vR[i])
    #print(yy)
    #各区間の面積を求める
    ans=0
    for t,y0,y1,v in zip(tt,yy,yy[1:],vv):
        h=(t+y0+y1)/2
        ans+=((h+y0)*(h-y0)+(h+y1)*(h-y1))/2
        if h>v:ans-=(h-v)**2
    print(ans)

main()
