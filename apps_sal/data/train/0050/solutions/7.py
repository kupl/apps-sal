import itertools
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    ones = a.count(1)
    twos = a.count(2)
    
    a1 = a[:n][::-1]
    a2 = a[n:]
    
    target = ones - twos
    
    a1 = [[-1,1][x==1]for x in a1]
    a1 = [0] + list(itertools.accumulate(a1))
    a2 = [[-1,1][x==1]for x in a2]
    a2 = [0] + list(itertools.accumulate(a2))
    
    a2v = defaultdict(lambda: 2*n+1)
    for i2, x2 in enumerate(a2):
        a2v[x2] = min(a2v[x2], i2)
    best = 2*n
    
    for i1, x1 in enumerate(a1):
        best = min(best, i1+a2v[target-x1])
    
    print(best)

