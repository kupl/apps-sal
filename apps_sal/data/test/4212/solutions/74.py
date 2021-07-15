from itertools import combinations_with_replacement as comb_r
n,m,q=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(q)]

mx=0
for x in comb_r(range(1,m+1),n):
    sm=0
    for y in lst:
        if x[y[1]-1]-x[y[0]-1]==y[2]:
            sm+=y[3]
    if mx<sm : mx=sm

print(mx)
