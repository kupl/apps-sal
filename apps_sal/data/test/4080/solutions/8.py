import sys
import copy
input = sys.stdin.readline

n,m=map(int,input().split())
A=list(map(int,input().split()))

LR=[list(map(int,input().split())) for i in range(m)]


MLIST=[]
for l,r in LR:
    MLIST.append(l)
    MLIST.append(r)

MLIST=list(set(MLIST))
MLIST.sort()
MLIST.append(10**9)


MDICT=dict()
MLEN=len(MLIST)
for i in range(MLEN):
    MDICT[MLIST[i]]=i


MINUSLIST=[[0]*(MLEN*2-1) for i in range(MLEN)]

for l,r in LR:
    for j in range(MDICT[l],MDICT[r]+1):
        for k in range(MDICT[l]*2+1,MDICT[r]*2+2):
            MINUSLIST[j][k]+=1
            
#print(MLIST)
#print(MINUSLIST)


A_m=[[float("inf"),-float("inf")] for i in range(MLEN*2-1)]

if MLIST[0]!=1:
    A_m[0]=[min(A[:MLIST[0]-1]),max(A[:MLIST[0]-1])]
#if MLIST[MLEN-2]!=n:
#    A_m[MLEN*2-2]=[min(A[MLIST[MLEN-2]:]),max(A[MLIST[MLEN-2]:])]

for i in range(MLEN-1):
    x=MLIST[i]-1
    y=MLIST[i+1]-1

    A_m[2*i+1]=[A[x],A[x]]
    if x+1!=y and x!=n-1:
        A_m[2*i+2]=[min(A[x+1:y]),max(A[x+1:y])]
    
def MINUS(A,B):
    MIN=float("inf")
    MAX=-float("inf")

    for i in range(MLEN*2-1):
        if MIN>A[i][0]-B[i]:
            MIN=A[i][0]-B[i]
        if MAX<A[i][1]-B[i]:
            MAX=A[i][1]-B[i]

    return MAX-MIN

ANSLIST=[0]*MLEN

for i in range(MLEN):
    ANSLIST[i]=MINUS(A_m,MINUSLIST[i])

print(max(ANSLIST))
target=MLIST[ANSLIST.index(max(ANSLIST))]

AN=[]
for i in range(m):
    z,w=LR[i]
    if z<=target<=w:
        AN.append(i+1)

print(len(AN))
for a in AN:
    print(a,end=" ")


