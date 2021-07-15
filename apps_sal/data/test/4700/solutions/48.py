n,m=map(int,input().split())
way=[[] for i in range(n)]
H = list(map(int,input().split()))
for i in range(m):
    a,b=map(int,input().split())
    way[a-1].append(b-1)
    way[b-1].append(a-1)

for i in range(n):
    way[i]=list(set(way[i]))

ans=0
for i in range(n):
    high=True
    for j in way[i]:
        if H[i]<=H[j]:
            high=0
            break
    if high:
        ans+=1
print(ans)
