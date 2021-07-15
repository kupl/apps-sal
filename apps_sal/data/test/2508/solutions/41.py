H,W,K=list(map(int,input().split()))
x1,y1,x2,y2=list(map(int,input().split()))
C=[]
nx=set([])

for _ in range(H):
    C.append(list(input()))

def keiro(x,y,k):
    i=1
    while True:
        if y+i>W-1 or C[x][y+i]!='.' or i>k:
            break
        else:
            if (x,y+i) not in nx:
                nx.add((x,y+i))
            i+=1
    
    i=1
    while True:
        if y-i<0 or C[x][y-i]!='.' or i>k:
            break
        else:
            if (x,y-i) not in nx:
                nx.add((x,y-i))
            i+=1
    
    i=1
    while True:
        if x+i>H-1 or C[x+i][y]!='.' or i>k:
            break
        else:
            if (x+i,y) not in nx:
                nx.add((x+i,y))
            i+=1
    
    i=1
    while True:
        if x-i<0 or C[x-i][y]!='.' or i>k:
            break
        else:
            if (x-i,y) not in nx:
                nx.add((x-i,y))
            i+=1

    return 0

C[x1-1][y1-1]=0
keiro(x1-1,y1-1,K)
taisho=nx.copy()
result=1
for j in nx:
    C[j[0]][j[1]]=result

while C[x2-1][y2-1]=='.':
    nx=set([])
    if len(taisho)==0 or result>10**6:
        result=-1
        break
    for l in taisho:
        keiro(l[0],l[1],K)
    result+=1
    for j in nx:
        C[j[0]][j[1]]=result
    taisho=nx.copy()

print(result)

