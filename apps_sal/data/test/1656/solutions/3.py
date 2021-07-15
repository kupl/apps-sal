import sys
input = sys.stdin.readline

s=input().strip()
ANS=0
BEFORE=0
OCOUNT=0

LEN=len(s)

for i in range(1,LEN):
    if s[i]=="v" and s[i-1]=="v":
        BEFORE+=1

        ANS+=OCOUNT

    if s[i]=="o":
        OCOUNT+=BEFORE

print(ANS)

    

