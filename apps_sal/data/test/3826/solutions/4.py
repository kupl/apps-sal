import sys
import copy
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

from collections import Counter

C=Counter(A)
for a in A:
    if C[a]<=1:
        del C[a]



if not(C):
    print(0)
    return

ANS=n-1

for i in range(n):
    D=copy.deepcopy(C)

    for j in range(i,n):
        if D[A[j]]>=1:
            D[A[j]]-=1

        if D[A[j]]==1:
            del D[A[j]]

        if not(D):
            ANS=min(ANS,j-i+1)
            break

    #print(i,j,D,ANS)

print(ANS)
            

