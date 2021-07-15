T=int(input())

for t in range(T):
    L=[]
    for i in range(8):
        L.append(input())
    Moves1=[]
    Moves2=[]
    K=[]
    for i in range(8):
        Moves1.append([-1]*8)
        Moves2.append([-1]*8)
        for j in range(8):
            if(L[i][j]=='K'):
                K.append((i,j))
    Now=K[0]
    Explored=[(Now[0],Now[1],0)]
    Moves1[Now[0]][Now[1]]=0
    while(len(Explored)!=0):
        x=Explored[0][0]
        y=Explored[0][1]
        p=Explored[0][2]
        Explored.pop(0)
        if(x-2>=0 and y-2>=0):
            if(Moves1[x-2][y-2]==-1):
                Moves1[x-2][y-2]=1-p
                Explored.append((x-2,y-2,1-p))
        if(x+2<8 and y-2>=0):
            if(Moves1[x+2][y-2]==-1):
                Moves1[x+2][y-2]=1-p
                Explored.append((x+2,y-2,1-p))
        if(x-2>=0 and y+2<8):
            if(Moves1[x-2][y+2]==-1):
                Moves1[x-2][y+2]=1-p
                Explored.append((x-2,y+2,1-p))
        if(x+2<8 and y+2<8):
            if(Moves1[x+2][y+2]==-1):
                Moves1[x+2][y+2]=1-p
                Explored.append((x+2,y+2,1-p))
    Now=K[1]
    Explored=[(Now[0],Now[1],0)]
    Moves2[Now[0]][Now[1]]=0
    while(len(Explored)!=0):
        x=Explored[0][0]
        y=Explored[0][1]
        p=Explored[0][2]
        Explored.pop(0)
        if(x-2>=0 and y-2>=0):
            if(Moves2[x-2][y-2]==-1):
                Moves2[x-2][y-2]=1-p
                Explored.append((x-2,y-2,1-p))
        if(x+2<8 and y-2>=0):
            if(Moves2[x+2][y-2]==-1):
                Moves2[x+2][y-2]=1-p
                Explored.append((x+2,y-2,1-p))
        if(x-2>=0 and y+2<8):
            if(Moves2[x-2][y+2]==-1):
                Moves2[x-2][y+2]=1-p
                Explored.append((x-2,y+2,1-p))
        if(x+2<8 and y+2<8):
            if(Moves2[x+2][y+2]==-1):
                Moves2[x+2][y+2]=1-p
                Explored.append((x+2,y+2,1-p))
    valid=False
    for i in range(8):
        for j in range(8):
            if(Moves1[i][j]!=-1 and Moves1[i][j]==Moves2[i][j] and L[i][j]!="#"):
                valid=True
    if(valid):
        print("YES")
    else:
        print("NO")
    if(t!=T-1):
        s=input()

