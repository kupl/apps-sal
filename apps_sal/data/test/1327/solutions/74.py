n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for _ in range(n)]
maxi=0
for i in range(2**3):
    idx=[]
    for j in range(3):
        if (i>>j)&1:
            idx.append(j)
    arr=[]
    for j in range(n):
        s=0
        for k in range(3):
            if k in idx:
                s-=xyz[j][k]
            else:
                s+=xyz[j][k]
        arr.append((s,j))
    arr.sort(reverse=True)
    x,y,z=0,0,0
    for j in range(m):
        x+=xyz[arr[j][1]][0]
        y+=xyz[arr[j][1]][1]
        z+=xyz[arr[j][1]][2]
    maxi=max(maxi,abs(x)+abs(y)+abs(z))
print(maxi)
