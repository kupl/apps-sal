import itertools
import math
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
l=[]
for i in range(0,N):
    l.append(i)
p=list(itertools.permutations(l,N))
z=0
for j in range(0,len(p)):
    for k in range(0,N-1):
        z=z+math.sqrt(pow(x[p[j][k]]-x[p[j][k+1]],2)+pow(y[p[j][k]]-y[p[j][k+1]],2))
ans=z/len(p)
print(ans)

