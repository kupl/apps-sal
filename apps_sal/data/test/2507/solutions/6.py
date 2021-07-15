#import sys
import numpy as np
#input = sys.stdin.readline

def main():
    n, k=map(int, input().split())
    a=np.array(list(map(int, input().split())), dtype=np.int64)
    f=np.array(list(map(int, input().split())), dtype=np.int64)
    a=np.sort(a)
    f=np.sort(f)[::-1]
    l,r=0,10**12
    while l<=r:
        m=(l+r)//2
        tr=np.clip(a-m//f,0,None).sum()
        if tr>k:
            l=m+1
        else:
            r=m-1
    print(l)

def __starting_point():
    main()
__starting_point()
