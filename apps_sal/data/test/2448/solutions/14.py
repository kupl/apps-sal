import sys
input = sys.stdin.readline

t=int(input())

for testcases in range(t):
    n=int(input())
    a,b,c=list(map(int,input().split()))
    B=input().strip()

    R=B.count("R")
    P=B.count("P")
    S=B.count("S")

    if min(b,R)+min(c,P)+min(a,S)>=n/2:
        print("YES")
    else:
        print("NO")
        continue

    ANS=[0]*n

    R0=min(a,S)
    P0=min(b,R)
    S0=min(c,P)

    R1=a-R0
    P1=b-P0
    S1=c-S0

    for i in range(n):
        if B[i]=="S" and R0>0:
            ANS[i]="R"
            R0-=1
        elif B[i]=="R" and P0>0:
            ANS[i]="P"
            P0-=1
        elif B[i]=="P" and S0>0:
            ANS[i]="S"
            S0-=1

    for i in range(n):
        if ANS[i]==0:
            if R1>0:
                R1-=1
                ANS[i]="R"

            elif P1>0:
                P1-=1
                ANS[i]="P"

            else:
                S1-=1
                ANS[i]="S"

    print("".join(ANS))


