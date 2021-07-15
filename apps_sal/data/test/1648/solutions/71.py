from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, list(range(n, n - r, -1)))
    under = reduce(mul, list(range(1,r + 1)))
    return (over // under)%(10**9+7)
N,k=list(map(int,input().split()))
l=N-k
for i in range(1,k+1):
    if l<i-1:
        print((0))
    else:
        num1=l-(i-1)
        print(((cmb(k-1,i-1)*cmb(num1+i,i))%(10**9+7)))

