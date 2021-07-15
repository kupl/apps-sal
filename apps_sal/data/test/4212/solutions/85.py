import itertools
n,m,q=map(int,input().split())
req=[list(map(int,input().split())) for _ in range(q)]
a=itertools.combinations_with_replacement(range(1,m+1),n)
ans=0
for i in a:
    point=0
    for j in req:
        if i[j[1]-1]-i[j[0]-1]==j[2]:
            point+=j[3]
    ans=max(ans,point)
print(ans)
