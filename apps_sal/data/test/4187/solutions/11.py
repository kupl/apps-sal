import sys
input = sys.stdin.readline


n=int(input())
A=list(map(int,input().split()))

A+=A
A+=A

ANS=0
REST=0

for a in A:
    if a==1:
        REST+=1
    else:
        if ANS<REST:
            ANS=REST
        REST=0

print(ANS)

