from functools import reduce
import sys

#f = open('test', 'r')
#sys.stdin = f
m = int(input())
p = 10**9 + 7
dividors = [int(x) for x in input().split()]
D = {}
for d in dividors:
    if d in D:
        D[d] += 1
    else:
        D[d] = 1
prod = reduce(lambda x,y : x*y%p, dividors)
deg = reduce(lambda x,y : x*y, (d+1 for d in list(D.values())))
if deg % 2:
    prod = reduce(lambda x,y : x*y%p, (pow(d, i//2, p) for d,i in list(D.items())))
    ans = pow(prod, deg%(p-1), p)
else:
    ans = pow(prod, (deg//2)%(p-1), p)

print(ans)

