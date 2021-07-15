def main():
    import bisect
    import numpy as np
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    l = np.array(l)
    def bise(x):
        y = np.searchsorted(l,x-l)
        return n*n-y.sum()

    left = -1
    right = l[-1]*2+1

    while right > left+1:
        mid = (right+left)//2
        
        if bise(mid) >= k:
            left = mid
        else:
            right = mid
    ans = 0
    
    acc = np.zeros(n+1,np.int64)
    acc[1:] = l.cumsum()
    x = np.searchsorted(l,right-l)
    count = n*n-x.sum()
    ans = (acc[-1]-acc[x]).sum() + (l*(n-x)).sum()

    print(ans-(count-k)*left)
def __starting_point():
    main()
__starting_point()
