#parsea una línea
def parser():
    return [int(x) for x in input().split()]

#Método usado para contar las universidades en cada subárbol
def DFS():
    visited[0]=True
    stack=[]
    introduction_order=[]
    stack.append(0)
    while len(stack)>0:
        v=stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u]=v
                visited[u]=True
                if university_in_city[u]:
                    count_universities_subtree[u]+=1
                stack.append(u)
                introduction_order.append(u)
    
    #Recorriendo para saber la cantidad de universidades que hay en el subarbol de cada vertice
    for v in introduction_order[::-1]:
        count_universities_subtree[pi[v]]+=count_universities_subtree[v]

#Recibiendo los valores de n y k
n,k=parser()
#visitados
visited=[False for x in range(n)]
#padres
pi=[0 for x in range(n)]
#universidades en el subarbol
count_universities_subtree=[0 for x in range(n)]
#universidad en la ciudad
university_in_city=[False for x in range(n)]

#Recibiendo las ciudades que tienen universidades
cities_universities=parser()
for i in cities_universities:
    university_in_city[i-1]=True

#Armando el árbol que representa a Treeland
adjacents_list=[[] for x in range(n)]
for i in range(n-1):
    #Leyendo una arista
    edge=parser()
    adjacents_list[edge[0]-1].append(edge[1]-1)
    adjacents_list[edge[1]-1].append(edge[0]-1)

DFS()

#Calculando el total
total=0
for i in range(1,n):
    total+=min(count_universities_subtree[i],2*k-count_universities_subtree[i])

#Imprimiendo el resultado
print(total)
