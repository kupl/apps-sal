import sys
import math
from collections import defaultdict

def print_graph(graph):
    for key, values in graph.items():
        [print(key,nodo) for nodo in values]

def BFS(graph, n, start, end):
    #print("==================")
    #print("Partiendo BFS:")
    #print("Nodo Start:", start)
    #print("Nodo end:", end)
    q = [ (start,0) ]
    visited = [False for x in range(n)]
    visited[start] = True
    while (len(q) >0):
        aux = q.pop(0)
        actual = aux[0]
        peso = aux[1]+1
        #print("===========")
        #print("Nodo Actual:",actual)
        for vecino in graph[actual]:
            
            #saltamos el arco base
            if not visited[vecino] and not ((actual == start and end == vecino) or (vecino == start and end == actual)):
                #print("Vecino:",vecino)
                q.append( (vecino, peso) )
                visited[vecino] = True
                if vecino == end:
                    peso+=1
                    #print("PESO FINAL:", peso)
                    return peso
        
        #print("peso hasta el momento:", peso)
    return -1    
 
lines = sys.stdin.read().split("\n")
lines.pop(-1)
#lines = ["50", "65600 17825792 0 288230376285929472 16392 0 0 16896 0 0 10486272 140737488355330 65537 171798691840 571746046443520 0 0 33024 0 2052 36028797155278848 36028805608898560 0 0 562967133290496 0 0 0 146028888064 281474976710660 0 288230376151711746 8388864 0 17180393472 0 0 0 68719476737 34376515584 0 299067162755072 68719478784 0 9007199255789568 140737488879616 9007199254773760 8796093022272 4294967304 17596481011712"]
#lines = ["4", "3 6 28 9"]
n = int(lines[0].strip())
#nodos_int = [  int(x) for x in lines[1].strip().split(" ")]
nodos = [  "{0:b}".format(int(x)).zfill(60) for x in lines[1].strip().split(" ")]
graph = dict()
vertex = []
 
for i in range(n):
    graph[i] = []
    
for bit in range(60):
    count = 0
    q = []
    for index in range(n):
        if nodos[index][bit] =='1':
            count+=1
            q.append(index)
    if count==2:
        graph[q[0]] += [q[1]]
        graph[q[1]] += [q[0]]
        vertex.append([q[0],q[1]])
    if count>2:
        print(3)
        return
 
##print(vertex)
##print(graph)
        
minimo = -1
for index in range(n):
    while len(vertex) > 0:
        a,b = vertex.pop(0)
        peso = BFS(graph, n ,a,b)
        if (peso > 0):
            if minimo == -1:
                minimo = peso
            elif peso<minimo:
                minimo = peso
        
print(minimo)
#print_graph(graph)

