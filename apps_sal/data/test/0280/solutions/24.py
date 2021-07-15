import sys
input = sys.stdin.readline
from operator import itemgetter
import bisect

N,M=map(int,input().split())
W=list(map(int,input().split()))
B=[tuple(map(int,input().split())) for i in range(M)]

MIN=1<<60
for l,v in B:
    MIN=min(MIN,v)

if MIN<max(W):
    print(-1)
    return

B2=[]
for x,y in B:
    B2.append([y,x])
B2.sort(key=itemgetter(0))

B3=[B2[0]]
for x,y in B2[1:]:
    if y<=B3[-1][1]:
        continue
    else:
        B3.append([x,y])

B3=[[0,0]]+B3
B3.append([1<<60,B3[-1][1]])

from itertools import permutations

L=list(permutations(range(N)))
ANS=1<<60

for l in L:
    W2=[W[l[i]] for i in range(N)]
    DP=[0]*(N+1)

    for i in range(N):
        S=W2[i]
        for j in range(i+1,N):
            S+=W2[j]
            x=bisect.bisect(B3,[S,0])

            DP[j]=max(DP[j],DP[i]+B3[x-1][1])
       
    ANS=min(ANS,DP[N-1])
print(ANS)
