from collections import deque

#parser
def parser():
    return [int(x) for x in input().split()]

def DFS_Discriminiting():
    #visitados
    visited=[False for x in range(n)]
    visited[numbers_of_attacked_cities[0]]=True
    stack=[]
    intrudoction_order=[]
    stack.append(numbers_of_attacked_cities[0])
    while len(stack)>0:
        v=stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u]=v
                visited[u]=True
                if attacked_city[u]:
                    count_attacked_cities_subtree[u]+=1
                stack.append(u)
                intrudoction_order.append(u)    
    for v in intrudoction_order[::-1]:
        count_attacked_cities_subtree[pi[v]]+=count_attacked_cities_subtree[v]
        if count_attacked_cities_subtree[v]==0:
            important_cities[v]=False

def DFS_Heigths():
    #visitados
    visited=[False for x in range(n)]
    visited[numbers_of_attacked_cities[0]]=True
    stack=[]
    intrudoction_order=[]
    stack.append(numbers_of_attacked_cities[0])
    while len(stack)>0:
        v=stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u]=v
                visited[u]=True
                stack.append(u)
                intrudoction_order.append(u)
    for v in intrudoction_order[::-1]:
        if heights1[pi[v]] < heights1[v]+1:
            heights2[pi[v]]=heights1[pi[v]]
            heights1[pi[v]]=heights1[v]+1
        elif heights2[pi[v]]<heights1[v]+1:
            heights2[pi[v]]=heights1[v]+1

def Distance_Root(s):
    for v in adjacents_list[s]:
        if heights1[v]+1>distances1[s]:
            distances2[s]=distances1[s]
            distances1[s]=heights1[v]+1
        elif heights1[v]+1>distances2[s]:
            distances2[s]=heights1[v]+1

def DFS_Distances():
    #visitados
    visited=[False for x in range(n)]
    visited[numbers_of_attacked_cities[0]]=True
    stack=[]
    stack.append(numbers_of_attacked_cities[0])
    Distance_Root(numbers_of_attacked_cities[0])
    while len(stack)>0:
        v=stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u]=v
                visited[u]=True
                determinate=False
                stack.append(u)
                if heights1[u]+1==distances1[v]:
                    if heights1[u]+1>distances2[v]:
                        determinate=True
                        distances1[u]=max(heights1[u],distances2[v]+1)
                        if distances1[u]==heights1[u]:
                            distances2[u]=max(distances2[v]+1,heights2[u])
                        else:
                            distances2[u]=heights1[u]
                if not determinate:
                    distances1[u]=distances1[v]+1
                    distances2[u]=heights1[u]

def BFS(s):
    distance=[-1 for x in range(n)]
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


n,m=parser()
#Creando los arrays necesarios para la ejecucion de DFS
#padres
pi=[0 for x in range(n)]
#ciudades atacadas en el subarbol
count_attacked_cities_subtree=[0 for x in range(n)]
#ciudad atacada o no atacada
attacked_city=[False for x in range(n)]
#ciudades_que_son atacadas o sirven para llegar a las mismas
important_cities=[True for x in range(n)]

adjacents_list=[[] for x in range(n)]
for i in range(n-1):
    edge=parser()
    adjacents_list[edge[0]-1].append(edge[1]-1)
    adjacents_list[edge[1]-1].append(edge[0]-1)

#numero de ciudades atacadas
numbers_of_attacked_cities=[]
for i in parser():
    numbers_of_attacked_cities.append(i-1)

if m==1:
    print(numbers_of_attacked_cities[0]+1)
    print(0)
    return

#marcando las ciudades atacadas
for i in numbers_of_attacked_cities:
    attacked_city[i]=True

DFS_Discriminiting()

adjacents_list=[[] for x in range(n)]

count_edges=0
for v in range(n):
    if v==numbers_of_attacked_cities[0]:
        continue
    elif important_cities[v] and important_cities[pi[v]]:
        adjacents_list[v].append(pi[v])
        adjacents_list[pi[v]].append(v)
        count_edges+=1

#padres
pi=[0 for x in range(n)]

#alturas
heights1=[0 for x in range(n)]
heights2=[0 for x in range(n)]

DFS_Heigths()

#distances
distances1=[0 for x in range(n)]
distances2=[0 for x in range(n)]

DFS_Distances()

lower=distances1[numbers_of_attacked_cities[0]]
for i in range(n):
    if important_cities[i] and lower>distances1[i]:
        lower=distances1[i]

centers=[]
for i in range(n):
    if distances1[i]==lower:
        centers.append(i)


posibles_begin_cities=[]

for i in centers:
    distances_center=BFS(i)
    max_distance=0
    for j in range(n):
        if distances_center[j]>max_distance:
            max_distance=distances_center[j]
    for j in range(n):
        if distances_center[j]==max_distance:
            posibles_begin_cities.append(j)


print(min(posibles_begin_cities)+1)

print(2*count_edges-(distances1[centers[0]]+distances2[centers[0]]))
