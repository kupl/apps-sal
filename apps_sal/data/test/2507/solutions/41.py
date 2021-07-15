def main():
    import sys
    input=sys.stdin.readline
    import numpy as np

    n,k=list(map(int,input().split()))
    A=np.array(input().split(),dtype=np.int64)
    F=np.array(input().split(),dtype=np.int64)
    A.sort()
    F.sort()
    F=F[::-1]

    def ok(x): #チームの成績をxとするような修行の仕方が存在するか
        cnt=np.maximum(0,A-x//F).sum()
        return cnt<=k
    
    l=-1
    r=10**12+1
    while r-l>1:
        mid=(r+l)//2
        if ok(mid):
            r=mid
        else:
            l=mid
    print(r)   

def __starting_point():
    main()


__starting_point()
