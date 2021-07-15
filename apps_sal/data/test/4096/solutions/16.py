import sys

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))

if sum(A)<m:
    print(-1)
    return

A.sort(reverse=True)

MIN=1
MAX=n

while MIN!=MAX:
    d=(MIN+MAX)//2


    ANS=0
    j=0
    count=0
    for a in A:
        if a<=j:
            continue
        
        ANS+=(a-j)
        count+=1

        if count==d:
            j+=1
            count=0

    #print(d,ANS)

    if ANS>=m:
        MAX=d
    else:
        MIN=d+1
print(MIN)
            

