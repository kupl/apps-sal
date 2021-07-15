n,c=map(int,input().split())
imos=[[0 for i in range(c)] for j in range(10**5+1)]#1~10**5+1
for i in range(n):
    s,t,_c=map(int,input().split())
    imos[s-1][_c-1]+=1
    imos[t][_c-1]-=1
for i in range(1,10**5+1):
    for j in range(c):
        imos[i][j]+=imos[i-1][j]
imosans=[0]*(10**5+1)
for i in range(10**5+1):
    for j in range(c):
        imosans[i]+=(imos[i][j]>=1)
print(max(imosans))
