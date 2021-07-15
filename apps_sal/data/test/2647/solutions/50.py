H,W=list(map(int,input().split()))

sq=[list(input()) for i in range(H)]

pos=[[0,0,0]]
g=True

while pos!=[]:
    y,x,depth=pos.pop(0)

    if y==H-1 and x==W-1:
        g=False
        break
    
    if x-1>=0:
        if sq[y][x-1]==".":
            pos.append([y,x-1,depth+1])
            sq[y][x-1]="!"
    if x+1<=W-1:
        if sq[y][x+1]==".":
            pos.append([y,x+1,depth+1])
            sq[y][x+1]="!"
    if y-1>=0:
        if sq[y-1][x]==".":
            pos.append([y-1,x,depth+1])
            sq[y-1][x]="!"
    if y+1<=H-1:
        if sq[y+1][x]==".":
            pos.append([y+1,x,depth+1])

if g==True:
    print((-1))
else:
    temp=0
    for k in range(H):
        for m in range(W):
            if sq[k][m]=="#":
                temp+=1


    print((H*W-temp-depth-1))

