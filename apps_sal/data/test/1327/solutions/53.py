import sys,math,collections,itertools
input = sys.stdin.readline

x=0
y=0
z=0
xyz=[]
N,M=list(map(int,input().split()))
for _ in range(N):
    x0,y0,z0 = list(map(int,input().split()))
    x+=x0
    y+=y0
    z+=z0
    xyz.append([x0,y0,z0])
lmn =[]

for x0,y0,z0 in xyz:
    tmp = [x0,y0,z0]
    for fx in [-1,1]:
        for fy in [-1,1]:
            for fz in [-1,1]:
                tmp.append(x0*fx+y0*fy+z0*fz)
    lmn.append(tmp)

ans = 0
for i in range(8):
    lmn.sort(key = lambda x:-x[i+3])
    x=0
    y=0
    z=0
    for j in range(M):
        x += lmn[j][0]
        y += lmn[j][1]
        z += lmn[j][2]
    ans = max(ans,abs(x)+abs(y)+abs(z))
print(ans)
        
    

