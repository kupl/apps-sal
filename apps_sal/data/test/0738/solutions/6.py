import sys
input = sys.stdin.readline

A,B,C,D=list(map(int,input().split()))

def sm2(x,A,B,C):
    MIN=A+B
    MAX=B+C
    fr=min(B-A,C-B)

    sa=min(x-MIN,MAX-x,fr)

    return sa+1

def calc(x,C,D):
    return max(0,min(x-1,D)-C+1)

ANS=0
for x in range(A+B,B+C+1):
    smplus=sm2(x,A,B,C)
    ANS+=smplus*calc(x,C,D)

    #print(x,smplus,ANS)

print(ANS)

    

