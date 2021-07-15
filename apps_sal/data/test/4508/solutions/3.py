
import sys

def get_new_edges(graph):
    n = len(graph)
    far_vertex = []
    pi = [None]*n
    visit = [False]*n
    visit[0]
    queue = [[0,0]]
    i = 0    
    while True:
        if i >= len(queue): break
        current, d = queue[i]
        i += 1
        visit[current] = True
        for v in graph[current]:
            if not visit[v]:
                u = [v, d+1]
                pi[v] = current
                queue.append(u)
                if d+1 > 2:
                    far_vertex.append(u)
    
    far_vertex.sort(key=lambda x: -x[1])

    pos = [None]*n
    for i, e in enumerate(far_vertex):
        pos[e[0]] = i

    count = 0
    for i in range(len(far_vertex)):
        if not far_vertex[i]: continue
        vertex, depth = far_vertex[i]
        father = pi[vertex]
        count += 1
        if pos[father]:
            far_vertex[pos[father]] = None
        for u in graph[father]:
            if pos[u]:
                far_vertex[pos[u]] = None

    return count
    
def read_int_line():
    return list(map(int, sys.stdin.readline().split()))

vertex_count = int(input())
graph = [[] for _ in range(vertex_count)]

for i in range(vertex_count - 1):
    v1, v2 = read_int_line()
    v1 -= 1
    v2 -= 1
    graph[v1].append(v2)
    graph[v2].append(v1)

print(get_new_edges(graph))


    

