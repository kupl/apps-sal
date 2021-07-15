import itertools
import math

n=int(input())
xy=[[int(i) for i in input().split()] for _ in range(n)]
p = itertools.permutations(list(range(n)),n)

lenlist=[]
for v in p:
    len=0
    for i in range(n-1):
        len +=  ( (xy[v[i+1]][0]-xy[v[i]][0])**2 + (xy[v[i+1]][1]-xy[v[i]][1])**2 )**0.5
    lenlist.append(len)

print((sum(lenlist)/math.factorial(n)))

