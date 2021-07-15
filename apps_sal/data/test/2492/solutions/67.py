import sys
#sys.setrecursionlimit(10**9)
input = sys.stdin.readline

import numpy as np

n, k = list(map(int, input().split()))
A = np.array(input().split(), np.int64)
A = np.sort(A)

P = A[A>0]
Z = A[A==0]
N = A[A<0]

#t = n*(n-1)//2

def ok(x):
    # x以下になる組み合わせがk個以上
    cnt = 0
    #cnt += np.searchsorted(A, np.ceil(x/P), side='right').sum()
    cnt += np.searchsorted(A, x//P, side='right').sum()
    #cnt += n-np.searchsorted(A, np.floor(x/N), side='left').sum()
    cnt += (n-np.searchsorted(A, (-x-1)//(-N), side='right')).sum()
    if x >= 0:
        cnt += len(Z)*n
    cnt -= np.count_nonzero(A*A <= x)
    cnt = cnt//2
    if cnt >= k:
        return True
    else:
        return False

l = -10**18-1
r = 10**18+1
while l+1 < r:
    c = (l+r)//2
    if ok(c):
        r = c
    else:
        l = c
print(r)

