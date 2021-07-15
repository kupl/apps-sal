import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    S=input().strip()+"0"

    L=[]

    NOW=0
    for s in S:
        if s=="0":
            L.append(NOW)
            NOW=0
        else:
            NOW+=1

    L.sort(reverse=True)

    ANS=0

    for i in range(0,len(L),2):
        ANS+=L[i]

    print(ANS)
        

