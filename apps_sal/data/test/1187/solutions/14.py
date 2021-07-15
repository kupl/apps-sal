import sys
input = sys.stdin.readline

n,m=map(int,input().split())
EDGE=[tuple(map(int,input().split())) for i in range(m)]

E=[[] for i in range(n+1)]

# Kahnのアルゴリズム

EDGEIN=[0]*(n+1)# その点に入るEDGEの個数
EDGEOUTLIST=[[] for i in range(n+1)]# EDGEの行き先
for x,y in EDGE:
    EDGEIN[y]+=1
    EDGEOUTLIST[x].append(y)

from collections import deque
QUE = deque()

for i in range(1,n+1):
    if EDGEIN[i]==0:
        QUE.append(i)# 行き先のない点をQUEに入れる



TOP_SORT=[]
while QUE:
    x=QUE.pop()
    TOP_SORT.append(x)# 行き先がない点を答えに入れる
    for to in EDGEOUTLIST[x]:
        EDGEIN[to]-=1# 行き先がない点を削除し,そこから一歩先の点のEDGEINを一つ減らす.
        if EDGEIN[to]==0:
            QUE.appendleft(to)

if len(TOP_SORT)==n:
    print(1)
    print(*[1]*m)

else:
    print(2)
    for x,y in EDGE:
        if x>y:
            print(1,end=" ")
        else:
            print(2,end=" ")

