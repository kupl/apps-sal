from operator import add
from functools import reduce
N, M = map(int, input().split())
K = M - N
NL = reduce(add, range(1, K))
ans = NL - N
print(ans)
