#

import sys
from collections import deque
input=sys.stdin.readline

def main():
    H,W,K=map(int,input().split())
    x1,y1,x2,y2=map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    mas=[list(input()) for i in range(H)]

    dist=[[-1]*W for i in range(H)]
    dist[x1][y1]=0
    
    qu=deque([(x1,y1)])
    qup=qu.popleft
    qua=qu.append
    
    d=((-1,0),(1,0),(0,-1),(0,1))
    
    while(len(qu)>0):
        v=qup()
        for di in d:
            for i in range(1,K+1):
                nvh=v[0]+i*di[0]
                nvw=v[1]+i*di[1]
                if nvh<0 or nvh>=H or nvw<0 or nvw>=W or mas[nvh][nvw]=="@":
                    break
                if dist[nvh][nvw]!=-1 and dist[nvh][nvw]<=dist[v[0]][v[1]]:
                    break
                if dist[nvh][nvw]==-1:
                    dist[nvh][nvw]=dist[v[0]][v[1]]+1
                    qua((nvh,nvw))
    print(dist[x2][y2])
    
def __starting_point():
    main()
__starting_point()
