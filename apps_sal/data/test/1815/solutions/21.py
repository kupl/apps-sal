import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

from collections import Counter
C=Counter(A)

D=Counter(list(C.values()))
MAX=max(C.values())
MIN=min(C.values())

#print(C)
#print(D)

for i in range(n-1,-1,-1):
    if MAX==MIN+1 and D[MAX]==1:
        print(i+1)
        return

    if len(D)==2 and D[1]==1:
        print(i+1)
        return

    if len(D)==1 and D[1]>0:
        print(i+1)
        return

    if len(D)==1 and list(D.values())==[1]:
        print(i+1)
        return
        

    a=A[i]
    
    if MAX==C[a] and D[MAX]==1:
        MAX-=1
    if MIN==C[a]:
        MIN-=1
        
    D[C[a]]-=1
    if D[C[a]]==0:
        del D[C[a]]

    if MIN==0:
        MIN=min(D.keys())


    C[a]-=1

    if C[a]==0:
        del C[a]

    else:
        D[C[a]]+=1

    #print(C)
    #print(D)
    #print(MAX,MIN)

