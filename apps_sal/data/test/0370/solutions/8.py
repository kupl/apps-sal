import sys
input = sys.stdin.readline

K=int(input())
X,Y=list(map(int,input().split()))

if K%2==0 and (X+Y)%2==1:
    print((-1))
    return

ANS=[]
NOWX=0
NOWY=0

def dis(NOWX,NOWY,X,Y):
    return abs(NOWX-X)+abs(NOWY-Y)

def app():
    ANS.append((NOWX,NOWY))

if dis(NOWX,NOWY,X,Y)<K and dis(NOWX,NOWY,X,Y)%2==1:
    if X>0:
        NOWX-=K
        app()
    elif X<0:
        NOWX+=K
        app()
    elif Y>0:
        NOWY-=K
        app()
    elif Y<0:
        NOWY+=K
        app()
        

while dis(NOWX,NOWY,X,Y)>2*K:
    if X-NOWX>K:
        NOWX+=K
        app()
    elif NOWX-X>K:
        NOWX-=K
        app()
    elif Y-NOWY>K:
        NOWY+=K
        app()
    elif NOWY-Y>K:
        NOWY-=K
        app()



if dis(NOWX,NOWY,X,Y)!=K and dis(NOWX,NOWY,X,Y)%2==1:
    if X-NOWX>0:
        NOWX+=K
        app()
    elif NOWX-X>0:
        NOWX-=K
        app()
    elif Y-NOWY>0:
        NOWY+=K
        app()
    elif NOWY-Y>0:
        NOWY-=K
        app()



if dis(NOWX,NOWY,X,Y)==K:
    ANS.append((X,Y))

else:
    t=dis(NOWX,NOWY,X,Y)
    u=(K*2-t)//2

    if abs(NOWY-Y)<=abs(NOWX-X):

        if X<NOWX and Y>=NOWY:
                ANS.append((NOWX-(K-u),NOWY-u))
                ANS.append((X,Y))
        elif X<NOWX and Y<=NOWY:
                ANS.append((NOWX-(K-u),NOWY+u))
                ANS.append((X,Y))
                
        elif X>NOWX and Y>=NOWY:
                ANS.append((NOWX+(K-u),NOWY-u))
                ANS.append((X,Y))
        elif X>NOWX and Y<=NOWY:
                ANS.append((NOWX+(K-u),NOWY+u))
                ANS.append((X,Y))

    else:
        if X<=NOWX and Y>NOWY:
                ANS.append((NOWX+u,NOWY+(K-u)))
                ANS.append((X,Y))
        elif X<=NOWX and Y<NOWY:
                ANS.append((NOWX+u,NOWY-(K-u)))
                ANS.append((X,Y))
                
        elif X>=NOWX and Y>NOWY:
                ANS.append((NOWX-u,NOWY+(K-u)))
                ANS.append((X,Y))
        elif X>=NOWX and Y<NOWY:
                ANS.append((NOWX-u,NOWY-(K-u)))
                ANS.append((X,Y))
        
            
print((len(ANS)))
for x,y in ANS:
    print((x,y))
        
        

    
    

