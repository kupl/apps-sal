from collections import deque
from sys import stdin

# parsea una línea


def parser():
    return map(int, stdin.readline().split())

# Método usado para obtener los vértices por los que debe pasar Super M


def DFS_Discriminiting():
    visited = [False for x in range(n)]
    visited[numbers_of_attacked_cities[0]] = True
    stack = []
    introduction_order = []
    stack.append(numbers_of_attacked_cities[0])
    while len(stack) > 0:
        v = stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u] = v
                visited[u] = True
                if attacked_city[u]:
                    count_attacked_cities_subtree[u] += 1
                stack.append(u)
                introduction_order.append(u)
    for v in introduction_order[::-1]:
        count_attacked_cities_subtree[pi[v]] += count_attacked_cities_subtree[v]
        if count_attacked_cities_subtree[v] == 0:
            important_cities[v] = False

# Método usado para calcular las alturas


def DFS_Heigths():
    visited = [False for x in range(n)]
    visited[numbers_of_attacked_cities[0]] = True
    stack = []
    introduction_order = []
    stack.append(numbers_of_attacked_cities[0])
    while len(stack) > 0:
        v = stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)
                introduction_order.append(u)
    for v in introduction_order[::-1]:
        if heights1[pi[v]] < heights1[v] + 1:
            heights2[pi[v]] = heights1[pi[v]]
            heights1[pi[v]] = heights1[v] + 1
        elif heights2[pi[v]] < heights1[v] + 1:
            heights2[pi[v]] = heights1[v] + 1

# Método usado para calcular la primera y segunda distancia de la raíz


def Distance_Root(s):
    for v in adjacents_list[s]:
        if heights1[v] + 1 > distances1[s]:
            distances2[s] = distances1[s]
            distances1[s] = heights1[v] + 1
        elif heights1[v] + 1 > distances2[s]:
            distances2[s] = heights1[v] + 1

# Método usado para calcular la primera distancia y segunda distancia de cada vértice


def DFS_Distances():
    # visitados
    visited = [False for x in range(n)]
    visited[numbers_of_attacked_cities[0]] = True
    stack = []
    stack.append(numbers_of_attacked_cities[0])
    Distance_Root(numbers_of_attacked_cities[0])
    while len(stack) > 0:
        v = stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)
                determinate = False
                if heights1[u] + 1 == distances1[v]:
                    if heights1[u] + 1 > distances2[v]:
                        determinate = True
                        distances1[u] = max(heights1[u], distances2[v] + 1)
                        if distances1[u] == heights1[u]:
                            distances2[u] = max(distances2[v] + 1, heights2[u])
                        else:
                            distances2[u] = heights1[u]
                if not determinate:
                    distances1[u] = distances1[v] + 1
                    distances2[u] = heights1[u]

# Método usado para calcular las distancias de un vétice al resto de los vértices


def BFS(s):
    distance = [-1 for x in range(n)]
    distance[s] = 0
    q = deque()
    q.append(s)
    while len(q) > 0:
        v = q.popleft()
        for u in adjacents_list[v]:
            if distance[u] == -1:
                distance[u] = distance[v] + 1
                q.append(u)
    return distance


# Recibiendo los valores de n y m
n, m = parser()
# padres
pi = [0 for x in range(n)]
# ciudades atacadas en el subarbol
count_attacked_cities_subtree = [0 for x in range(n)]
# ciudad atacada o no atacada
attacked_city = [False for x in range(n)]
# ciudades_que_son atacadas o sirven para llegar a las mismas
important_cities = [True for x in range(n)]

# Armando el árbol que representa a Byteforces
adjacents_list = [[] for x in range(n)]
for i in range(n - 1):
    v1, v2 = parser()
    adjacents_list[v1 - 1].append(v2 - 1)
    adjacents_list[v2 - 1].append(v1 - 1)

# número de ciudades atacadas
numbers_of_attacked_cities = [x - 1 for x in parser()]
if m == 1:
    print(numbers_of_attacked_cities[0] + 1)
    print(0)
    return

# marcando las ciudades atacadas
for i in numbers_of_attacked_cities:
    attacked_city[i] = True

# Obteniendo las ciudades que recorre Super M
DFS_Discriminiting()

# Creando el nuevo árbol que representa el recorrido de Super M
adjacents_list = [[] for x in range(n)]

# Armando el nuevo árbol y contando sus aristas
count_edges = 0
for v in range(n):
    if v == numbers_of_attacked_cities[0]:
        continue
    elif important_cities[v] and important_cities[pi[v]]:
        adjacents_list[v].append(pi[v])
        adjacents_list[pi[v]].append(v)
        count_edges += 1

# alturas
heights1 = [0 for x in range(n)]
heights2 = [0 for x in range(n)]

# Calculando las alturas
DFS_Heigths()

# distancias
distances1 = [0 for x in range(n)]
distances2 = [0 for x in range(n)]

# Calculando las distancias
DFS_Distances()

# Hallando la mayor distancia de las primeras distancias
min_distance = distances1[numbers_of_attacked_cities[0]]
for i in range(n):
    if important_cities[i] and min_distance > distances1[i]:
        min_distance = distances1[i]

# Hallando el centro
center = []
for i in range(n):
    if distances1[i] == min_distance:
        center.append(i)

posibles_begin_cities = []

# Hallando la ciudad por la cual comenzar
for i in center:
    distances_center = BFS(i)
    max_distance = 0
    for j in range(n):
        if distances_center[j] > max_distance:
            max_distance = distances_center[j]
    for j in range(n):
        if distances_center[j] == max_distance:
            posibles_begin_cities.append(j)

# Imprimiendo la respuesta
print(min(posibles_begin_cities) + 1)
print(2 * count_edges - (distances1[center[0]] + distances2[center[0]]))
