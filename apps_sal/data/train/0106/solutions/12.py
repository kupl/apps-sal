import sys
input = sys.stdin.readline

Q=int(input())

for test in range(Q):
    n=int(input())
    LR=[list(map(int,input().split()))+[i] for i in range(n)]
    LR.sort()

    GR1=[LR[0][0],LR[0][1]]

    for i in range(1,n):
        l,r,_=LR[i]

        if r<GR1[0] or l>GR1[1]:
            ANS=i
            break
        else:
            GR1=[min(GR1[0],l),max(GR1[1],r)]

    else:
        print(-1)
        continue

    ANSLIST=[1]*n
    for j in range(ANS,n):
        ANSLIST[LR[j][2]]=2

    for a in ANSLIST:
        print(a,end=" ")
    print()

