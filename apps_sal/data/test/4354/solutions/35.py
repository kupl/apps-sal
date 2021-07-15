n,m=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
c=[list(map(int,input().split())) for _ in range(m)]
where=[]
for i in range(n):
    distance=10**9
    for j in range(m):
        if distance>abs(s[i][0]-c[j][0])+abs(s[i][1]-c[j][1]):
            distance=abs(s[i][0]-c[j][0])+abs(s[i][1]-c[j][1])
            w=j
    where.append(w+1)
[print(i) for i in where]
