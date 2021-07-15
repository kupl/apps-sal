from collections import defaultdict
from itertools import product

H,W,N = list(map(int,input().split()))

covered = defaultdict(int)
vector = [[-1,-1],[-1,0],[-1,1],[1,0],[1,1],[0,0],[0,-1],[0,1],[1,-1]]

for _ in range(N):
    a,b = list(map(int,input().split()))
    for dx,dy in vector:
        x = a+dx-1
        y = b+dy-1
        if 1 <= x < H-1 and 1 <= y < W-1:
            covered[(x,y)] += 1

values = [0]*10
for i in list(covered.values()):
    values[i] += 1

values[0] = (H-2)*(W-2) - sum(values)

for v in values:
    print(v)

