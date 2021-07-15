import sys
input = sys.stdin.readline

t=int(input())

for tests in range(t):
    n=int(input())
    S=input().strip()

    L=[1]

    for i in range(1,n):
        if S[i]==S[i-1]:
            L[-1]+=1
        else:
            L.append(1)
        
    de=0
    i=0
    ANS=0
    LEN=len(L)
    flag=0
    
    while de<LEN:

        if flag==0:            
            i=max(i,de)
            while i<LEN:
                if L[i]>1:
                    break
                else:
                    i+=1

            if i==LEN:
                flag=1
            else:
                L[i]-=1

        if flag==0:
            de+=1
            ANS+=1
        else:
            de+=2
            ANS+=1
    print(ANS)

        
        
        

