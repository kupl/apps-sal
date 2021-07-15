N,M=map(int,input().split())
K=M-N
from functools import reduce
from operator import add
NL=reduce(add,range(1,K))
ans=NL-N
print(ans)
