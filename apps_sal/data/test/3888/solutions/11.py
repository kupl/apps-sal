import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B=[A[0]]+[int(input()) for i in range(N-1)]

if N<=10:
    LIST=[[-1]*N for i in range(N)]
    LIST[0]=A
    for i in range(N):
        LIST[i][0]=B[i]

    for i in range(1,N):
        for j in range(1,N):
            SET={LIST[i-1][j],LIST[i][j-1]}

            if not (0 in SET):
                LIST[i][j]=0
            elif not (1 in SET):
                LIST[i][j]=1
            else:
                LIST[i][j]=2

    ZERO=0
    ONE=0
    TWO=0

    for i in range(N):
        ZERO+=LIST[i].count(0)
        ONE+=LIST[i].count(1)
        TWO+=LIST[i].count(2)

    print(ZERO,ONE,TWO)

    return

    


LIST1=[[-1]*N for i in range(4)]
LIST1[0]=A
LIST1[1][0]=B[1]
LIST1[2][0]=B[2]
LIST1[3][0]=B[3]

for i in range(1,4):
    for j in range(1,N):
        SET={LIST1[i-1][j],LIST1[i][j-1]}

        if not (0 in SET):
            LIST1[i][j]=0
        elif not (1 in SET):
            LIST1[i][j]=1
        else:
            LIST1[i][j]=2

LIST2=[[-1]*N for i in range(4)]
LIST2[0]=B
LIST2[1][0]=A[1]
LIST2[2][0]=A[2]
LIST2[3][0]=A[3]

for i in range(1,4):
    for j in range(1,N):
        SET={LIST2[i-1][j],LIST2[i][j-1]}

        if not (0 in SET):
            LIST2[i][j]=0
        elif not (1 in SET):
            LIST2[i][j]=1
        else:
            LIST2[i][j]=2

ZERO=0
ONE=0
TWO=0
k=1

for i in range(N-1,2,-1):
    if LIST1[3][i]==0:
        ZERO+=k
    elif LIST1[3][i]==1:
        ONE+=k
    else:
        TWO+=k
    k+=1

k=1
for i in range(N-1,3,-1):
    if LIST2[3][i]==0:
        ZERO+=k
    elif LIST2[3][i]==1:
        ONE+=k
    else:
        TWO+=k
    k+=1

ZERO+=LIST1[0].count(0)+LIST1[1].count(0)+LIST1[2].count(0)+LIST2[0][3:].count(0)+LIST2[1][3:].count(0)+LIST2[2][3:].count(0)
ONE+=LIST1[0].count(1)+LIST1[1].count(1)+LIST1[2].count(1)+LIST2[0][3:].count(1)+LIST2[1][3:].count(1)+LIST2[2][3:].count(1)
TWO+=LIST1[0].count(2)+LIST1[1].count(2)+LIST1[2].count(2)+LIST2[0][3:].count(2)+LIST2[1][3:].count(2)+LIST2[2][3:].count(2)

print(ZERO,ONE,TWO)
