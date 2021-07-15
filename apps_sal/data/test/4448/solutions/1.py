import sys
import bisect
import copy
input = sys.stdin.readline

n,m=list(map(int,input().split()))
K=[0]+list(map(int,input().split()))
SP=[list(map(int,input().split())) for i in range(m)]

SP2=[[] for i in range(n+1)]

for d,t in SP:
    SP2[t].append(d)

for i in range(n+1):
    SP2[i].sort()

SUM=sum(K)
MIN=SUM
MAX=SUM*2
MAXBUY=0

for day in range(MIN,MAX+1):

    DAYS=[[] for i in range(day+1)]

    for i in range(n+1):
        x=bisect.bisect_right(SP2[i],day)-1
        if x>=0:
            DAYS[SP2[i][x]].append(i)

    GOLD=0
    SUMK=SUM
    K2=copy.deepcopy(K)

    for d in range(1,day+1):
        GOLD+=1

        for t in DAYS[d]:
            DBUY=min(K2[t],GOLD,SUMK)
            K2[t]-=DBUY
            GOLD-=DBUY


    if GOLD>=sum(K2)*2:
        print(day)
        break




        
        

