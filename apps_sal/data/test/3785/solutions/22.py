from collections import deque as dq

class Graph:
    def __init__(self,n=0,m=0):
        self.g=[None for i in range(n)]
        self.vis=[[False for j in range(m)] for i in range(n)]
        self.dx=(1,0,-1,0)
        self.dy=(0,1,0,-1)

    def affiche(self):
        for i in range(len(self.g)):
            print("".join(self.g[i]))
    def readG(self,n):
        for i in range(n):
            self.g[i]=list(input())

    def get(self,i,j):
        return self.g[i][j]
            
    def dfsIt(self,u):
        nonlocal k,A
        L=dq()
        A=[]
        L.append(u)        
        while len(L)!=0:
            u=L.pop()
            self.vis[u[0]][u[1]]=True
            b=True
            for t in range(4):
                x=u[0]+self.dx[t]
                y=u[1]+self.dy[t]
                if x>=0 and x<n and y>=0 and y<m and not self.vis[x][y] and self.g[x][y]!='#':
                    self.vis[x][y]=True
                    L.append((x,y))
                    b=False
            if b and k>0:
                k-=1
                self.g[u[0]][u[1]]='X'
            else:
                A.append(u)
    
n,m,k=list(map(int,input().split()))
g=Graph(n,m)
g.readG(n)

def f():
    nonlocal n,m,g
    for i in range(n):
        for j in range(m):
            if g.get(i,j)=='.':
                return (i,j)
            
g.dfsIt(f())
while k!=0:
    k-=1
    u=A.pop()
    g.g[u[0]][u[1]]='X'

g.affiche()
    

