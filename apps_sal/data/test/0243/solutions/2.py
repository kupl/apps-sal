import sys
import heapq
from collections import deque

n,m,k=list(map(int,sys.stdin.readline().split()))
X=list(map(int,sys.stdin.readline().split()))
start=X[0]

EDGE=[list(map(int,sys.stdin.readline().split())) for i in range(m)]
COST_vertex=[[] for i in range(n+1)]
for i,j,w in EDGE:
    COST_vertex[i].append((j,w))
    COST_vertex[j].append((i,w))
    

MINCOST=[float("inf")]*(n+1)#求めたいリスト:startから頂点iへの最短距離
MINCOST[start]=0
checking=[(0,start)]#start時点のcostは0.最初はこれをチェックする.
while checking:
    cost,checktown=heapq.heappop(checking)
    #cost,checktownからの行き先をcheck.
    #cost最小なものを確定し,確定したものはcheckingから抜く.
    if MINCOST[checktown]<cost:#確定したものを再度チェックしなくて良い.
        continue    
    for to,co in COST_vertex[checktown]:
        if MINCOST[to]>max(MINCOST[checktown],co):
            MINCOST[to]=max(MINCOST[checktown],co)
            #MINCOST候補に追加
            heapq.heappush(checking,(max(MINCOST[checktown],co),to))


ANSLIST=[MINCOST[X[i]] for i in range(1,k)]

ANS=(str(max(ANSLIST))+" ")*k

sys.stdout.write(str(ANS)+"\n")
    


