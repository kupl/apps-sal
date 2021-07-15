import sys
input = sys.stdin.readline

N=int(input())
ARM=[list(map(int,input().split())) for i in range(N)]

OE=[(ARM[i][0]+ARM[i][1])%2 for i in range(N)]

if len(set(OE))==2:
    print((-1))
    return

if OE[0]==1:
    
    m=38
    print(m)
    print((*[1<<i for i in range(m)]))

    def URLD(x,y,m):
        
        if abs(x)>=abs(y):
            if x>=0:
                return "R",(x-(1<<m),y)
            else:
                return "L",(x+(1<<m),y)

        else:
            if y>=0:
                return "U",(x,y-(1<<m))
            else:
                return "D",(x,y+(1<<m))

    for x,y in ARM:
        ANS=[]
        for i in range(m-1,-1,-1):
            a,(x,y)=URLD(x,y,i)
            ANS.append(a)

        print(("".join(ANS[::-1])))
        
else:

    m=39
    print(m)
    print((1,*[1<<i for i in range(m-1)]))

    def URLD(x,y,m):
        
        if abs(x)>=abs(y):
            if x>=0:
                return "R",(x-(1<<m),y)
            else:
                return "L",(x+(1<<m),y)

        else:
            if y>=0:
                return "U",(x,y-(1<<m))
            else:
                return "D",(x,y+(1<<m))

    for x,y in ARM:
        ANS=[]
        for i in range(m-2,-1,-1):
            a,(x,y)=URLD(x,y,i)
            ANS.append(a)

        if x==1:
            ANS.append("R")
        elif x==-1:
            ANS.append("L")
        elif y==1:
            ANS.append("U")
        else:
            ANS.append("D")

        print(("".join(ANS[::-1])))
    
            

