import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))

MAP=[input().strip() for i in range(n)]


MINR=[1<<30]*n
MAXR=[-1]*n
MINC=[1<<30]*n
MAXC=[-1]*n

for i in range(n):
    for j in range(n):
        if MAP[i][j]=="B":
            MINR[i]=min(MINR[i],j)
            MAXR[i]=max(MAXR[i],j)
            MINC[j]=min(MINC[j],i)
            MAXC[j]=max(MAXC[j],i)

ALWAYS=0
for i in range(n):
    if MINR[i]==1<<30 and MAXR[i]==-1:
        ALWAYS+=1
    if MINC[i]==1<<30 and MAXC[i]==-1:
        ALWAYS+=1

ANS=[[0]*(n-k+1) for i in range(n-k+1)]

for j in range(n-k+1):
    NOW=0
    for i in range(k):

        if j<=MINR[i] and j+k-1>=MAXR[i] and MINR[i]!=1<<30 and MAXR[i]!=-1:
            NOW+=1

    ANS[0][j]+=NOW

    for i in range(n-k):

        if j<=MINR[i] and j+k-1>=MAXR[i] and MINR[i]!=1<<30 and MAXR[i]!=-1:
            NOW-=1


        if j<=MINR[i+k] and j+k-1>=MAXR[i+k] and MINR[i+k]!=1<<30 and MAXR[i+k]!=-1:
            NOW+=1

        ANS[i+1][j]+=NOW

for i in range(n-k+1):
    NOW=0
    for j in range(k):

        if i<=MINC[j] and i+k-1>=MAXC[j] and MINC[j]!=1<<30 and MAXC[j]!=-1:
            NOW+=1

    ANS[i][0]+=NOW

    for j in range(n-k):

        if i<=MINC[j] and i+k-1>=MAXC[j] and MINC[j]!=1<<30 and MAXC[j]!=-1:
            NOW-=1

        if i<=MINC[j+k] and i+k-1>=MAXC[j+k] and MINC[j+k]!=1<<30 and MAXC[j+k]!=-1:
            NOW+=1

        ANS[i][j+1]+=NOW

print(max([max(a) for a in ANS])+ALWAYS)
        
        
        

