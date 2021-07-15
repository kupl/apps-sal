from bisect import *
from numpy import *
N,K,*A = map(int,open(0).read().split())
B = [0]+list(cumsum(A))    
print(sum(N+1-bisect_left(B,K+B[n]) for n in range(N+1)))
