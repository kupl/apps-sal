import sys
input = sys.stdin.readline

t=int(input())
for testcases in range(t):
    n,T,a,b=list(map(int,input().split()))
    A=list(map(int,input().split()))
    L=list(map(int,input().split()))

    LCAN=[T]

    EASY=[]
    HARD=[]

    for i in range(n):
        if A[i]==0:
            EASY.append(L[i])
        else:
            HARD.append(L[i])

        if L[i]>1:
            LCAN.append(L[i]-1)

    LCAN=sorted(set(LCAN))

    EASY.sort()
    HARD.sort()

    #print(LCAN,a,b)
    #print(EASY)
    #print(HARD)
    #print()

    eind=0
    hind=0

    LENE=len(EASY)
    LENH=len(HARD)

    needtime=0
    ANS=0
    
    for time in LCAN:
        while eind<LENE and EASY[eind]<=time:
            needtime+=a
            eind+=1

        while hind<LENH and HARD[hind]<=time:
            needtime+=b
            hind+=1

        if time<needtime:
            continue
        else:
            rest=time-needtime
            score=eind+hind

            if (LENE-eind)*a>=rest:
                score+=rest//a
            else:
                score=LENE+hind
                rest-=(LENE-eind)*a

                score+=min(LENH-hind,rest//b)

            ANS=max(ANS,score)
            
    print(ANS)
                

        

            
        

    

