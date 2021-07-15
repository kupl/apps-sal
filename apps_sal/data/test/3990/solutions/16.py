from queue import PriorityQueue
class Graph:
    to=[]
    n=0
    def __init__(self,_n):
        self.to=[[False]*(_n+1)for i in range(_n+1)]
        self.n=_n
    def add_edge(self,s,t):
        self.to[s][t]=True
        self.to[t][s]=True
    def dijkstra(self):
        flag=self.to[1][self.n]==False
        ans=1
        dis=[-1]*(self.n+1)
        q=PriorityQueue()
        q.put((0,1))
        while q.qsize()>0:
            d1,pos=q.get()
            # print(pos,d1
            if dis[pos]!=-1:
                continue
            dis[pos]=d1

            for i in range(1,self.n+1):
                if self.to[pos][i]!=flag:
                    continue
                nx=i
                if nx==pos:
                    continue
                if dis[nx]==-1:
                    q.put((d1+1,nx))
        return dis[self.n]


gph=Graph(0)
N,M=[0]*2

def read_in():
    # file = open("input.txt")
    nonlocal N,M,gph
    N,M=[int(i)  for i in input().split()]

    gph=Graph(N)
    for i in range(M):
        # line=file.readline()
        s,t=[int(i)  for i in input().split()]

        gph.add_edge(s,t)
        # print(s,t,l)

read_in()

print(gph.dijkstra())
