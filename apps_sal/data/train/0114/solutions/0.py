import sys
input = sys.stdin.readline
import bisect

t=int(input())

for testcases in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    m=int(input())
    PS=[tuple(map(int,input().split())) for i in range(m)]

    PS.sort()
    K=[PS[-1]]

    for a,b in PS[::-1][1:]:
        if b<=K[-1][1]:
            continue
        else:
            K.append((a,b))

    K.reverse()

    ANS=1
    count=0
    countmax=n+1
    LEN=len(K)
    for a in A:
        x=bisect.bisect_left(K,(a,0))
        if x==LEN:
            print(-1)
            break
        elif K[x][1]>=count+1 and countmax>=count+1:
            count+=1
            countmax=min(countmax,K[x][1])
        else:
            ANS+=1
            count=1
            countmax=K[x][1]

        #print(a,count,countmax,ANS)
    else:
        print(ANS)
            
        
        

