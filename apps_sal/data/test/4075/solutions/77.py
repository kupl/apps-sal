n,m = list(map(int,input().split()))
ks = [[int(i) for i in input().split()] for _ in range(m)]
p = list(map(int,input().split()))

ans=0
for i in range(2**n):
    sw=[]
    on=0
    for j in range(n):
        sw.append(i>>j & 1)
    for k in range(m):
        if (sum( [sw[ks[k][j+1]-1] for j in range(ks[k][0])] ))%2 == p[k]:
            on +=1
    if on==m:
        ans +=1
print(ans)

