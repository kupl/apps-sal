N,C = map(int, input().split())
s =[0]*N
t =[0]*N
c =[0]*N
for i in range(N):
    s[i],t[i],c[i] = map(int, input().split())

imos = [[0]*int(1e5+20) for _ in range(31)]
for i in range(N):
    imos[c[i]][s[i]]+=1
    imos[c[i]][t[i]+1]-=1

ans = 0
for i in range(1,int(1e5+10)):
    sm = 0
    for j in range(31):
        imos[j][i]=imos[j][i-1]+ imos[j][i]
        if imos[j][i] >= 1:
            sm+=1
    ans = max(ans,sm)
print(ans)
