from collections import deque
from sys import stdin

#parser
def parser():
    return map(int, stdin.readline().split())
#Algoritmo BFS
def BFS(s):
    distance=[-1 for i in range(n)]
    distance[s]=0
    q=deque()
    q.append(s)
    while len(q)>0:
        v=q.popleft()
        for u in adjacents_list[v]:
            if distance[u] == -1:
                distance[u]=distance[v]+1
                q.append(u)
    return distance    

#Recibiendo los valores de n y x
n,x=parser()

#Armando el arbol
adjacents_list=[[] for i in range(n)]
for i in range(n-1):
    v1,v2=parser()
    adjacents_list[v1-1].append(v2-1)
    adjacents_list[v2-1].append(v1-1)

distance_Alice=BFS(0)

distance_Bob=BFS(x-1)

#Hallando el nodo mas alejado a Alice que puede alcanzar Bob antes que lo alcance Alice
max=0
for i in range(n):
    if max<distance_Alice[i] and distance_Bob[i]<distance_Alice[i]:
        max=distance_Alice[i]

print(max*2)
