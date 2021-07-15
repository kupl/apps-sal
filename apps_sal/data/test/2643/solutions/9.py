import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    k,q=MI()
    dd=LI()
    dd=np.array(dd,dtype="i8")
    for _ in range(q):
        n,x,m=MI()
        cc=dd%m
        zall=np.sum(cc==0)
        zlast=np.sum(cc[:(n-1)%k]==0)
        s=np.sum(cc)*((n-1)//k)
        r=np.sum(cc[:(n-1)%k])
        last=x%m+s+r
        no=last//m
        print(n-1-no-zall*((n-1)//k)-zlast)

main()

