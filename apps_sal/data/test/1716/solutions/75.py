n,m,q=map(int,input().split())
table=[[0]*(n+1)for i in range(n+1)]
for i in range(m):
    a,s=map(int,input().split())
    table[a][s]+=1
from itertools import accumulate
for i,v  in enumerate(table):
    table[i]=list(accumulate(v))

for i in range(n):
    for j in range(n):
        table[j+1][i+1]+=table[j][i+1]
for i in range(q):
    a,s=map(int,input().split())
    a-=1
    print((table[s][s]+table[a][a]-table[s][a]-table[a][s]))
