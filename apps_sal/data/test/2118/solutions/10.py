import os
import sys
import copy
num = 0
a = None
# sys.stdin = open(os.path.join(os.path.dirname(__file__),'35.in'))
k = None
def solve():
    nonlocal k,a
    n, k = map(lambda x:int(x), input().split())
    savek = copy.deepcopy(k)
    # print(a)
    a = [_+1 for _ in range(n)]

    def mgsort(l, r):
        nonlocal num,a,k
        mid = (l+r) >> 1
        if r - l == 1 or k == 1:
            return
        k -= 2
        a[l:mid] , a[mid:r] = a[mid:r] , a[l:mid]
        mgsort(l, mid)
        mgsort(mid, r)
    if k % 2 != 0:  
        mgsort(0, n)
        
    if k == 1:
        for i in a:
            print(i,sep=' ',end=' ')
    else:
        print(-1)
solve()
