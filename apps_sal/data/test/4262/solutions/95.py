import itertools
n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
r = list(itertools.permutations([i for i in range(1,n+1)]))
P , Q = (r.index(p)), (r.index(q))
print(abs(P-Q))
