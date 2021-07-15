from collections import defaultdict 
import sys
sys.setrecursionlimit(10000000)
#This class represents a undirected graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.visited =[False]*(self.V)
   
    
    def addEdge(self,gr): 
        self.graph=gr
        
   
   
    def isCyclicUtil(self,v,parent): 
  
        
        self.visited[v]= True
  
        
        for i in self.graph[v]: 
           
            if  self.visited[i]==False :  
                if(self.isCyclicUtil(i,v)): 
                    return True
            elif  parent!=i: 
                return True
          
        return False
           
   
    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self,p):
        if(self.isCyclicUtil(p,-1))== True:
            return True
          
        return False

n,m=list(map(int,input().split()))
g = Graph(n)
L=[[] for i in range(n)]
for i in range(m) :
    a,b=list(map(int,input().split()))
    L[a-1].append(b-1)
    L[b-1].append(a-1)
Visited=[False]*n
g.addEdge(L)
k=0
for i in range(n) :
    if Visited[i]==False :
        q=[i]
        while q :
            d=q.pop(0)
            Visited[d]=True
            for x in L[d] :
                if Visited[x]==False :
                    q.append(x)
                    Visited[x]=True
        try :
            if not g.isCyclic(i) :
                k+=1
        except Exception as e :
            print(e)
print(k)
        
  

