from sys import stdin

#Clase nodo
class Node():
    def __init__(self,value=None,prox=None):
        self.value=value
        self.prox=prox
#Clase cola      
class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.count=0

    def Enqueue(self,value):
        new_node=Node(value)
        self.count+=1
        if self.first is None:
            self.last=self.first=new_node
        else:
            self.last.prox=new_node
            self.last=new_node
    
    def Dequeue(self):
        value=self.first.value
        self.count-=1
        self.first=self.first.prox
        return value

#Parser
def parser():
    return map(int, stdin.readline().split())

#Algoritmo BFS
def BFS(s):
    if s==0:
        distance=distance_Alice
    else:
        distance=distance_Bob

    distance[s]=0
    q=Queue()
    q.Enqueue(s)
    while q.count>0:
        v=q.Dequeue()
        for u in adjacents_list[v]:
            if distance[u] == -1:
                distance[u]=distance[v]+1
                q.Enqueue(u)    

#Recibiendo los valores de n y x
n,x=parser()

#Creando los arrays necesarios para la ejecucion de DFS
#visitados
distance_Alice=[-1 for i in range(n)]
distance_Bob=[-1 for i in range(n)]

#Armando el arbol
adjacents_list=[[] for i in range(n)]
for i in range(n-1):
    v1,v2=parser()
    adjacents_list[v1-1].append(v2-1)
    adjacents_list[v2-1].append(v1-1)

BFS(0)

BFS(x-1)

#Hallando el nodo mas alejado a Alice que puede alcanzar Bob antes que lo alcance Alice
max=0
for i in range(n):
    if max<distance_Alice[i] and distance_Bob[i]<distance_Alice[i]:
        max=distance_Alice[i]

print(max*2)
