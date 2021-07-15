import sys
input = sys.stdin.readline

t=int(input())

for test in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    LEFT=[0]
    RIGHT=[0]

    for a in A[:n]:
        if a==1:
            LEFT.append(LEFT[-1]+1)
        else:
            LEFT.append(LEFT[-1]-1)

    for a in A[n:][::-1]:
        if a==1:
            RIGHT.append(RIGHT[-1]+1)
        else:
            RIGHT.append(RIGHT[-1]-1)

    #print(LEFT)
    #print(RIGHT)
    #print()

    MAXLEFT=[-1]*(2*n+1)
    MAXRIGHT=[-1]*(2*n+1)

    for i in range(n+1):
        MAXLEFT[LEFT[i]+n]=i
        MAXRIGHT[RIGHT[i]+n]=i
   
    #print(MAXLEFT)
    #print(MAXRIGHT)
    #print()

    ANS=0
    for i in range(2*n+1):
        if MAXLEFT[i]==-1 or MAXRIGHT[2*n-i]==-1:
            continue
        ANS=max(ANS,MAXLEFT[i]+MAXRIGHT[2*n-i])

    #print(ANS)
    print(2*n-ANS)

    
    

    

    
    

