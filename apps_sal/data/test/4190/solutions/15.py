from collections import Counter
n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
d=Counter(b)
ans=[]
e=list(range(1,n))+[0]
for i in a:
    v=(n-i)%n
    while d[v]==0:
        if d[e[v]]==0:
            e[v]=e[e[v]]
        v=e[v]
    d[v]-=1
    ans.append((i+v)%n)
print(*ans)
