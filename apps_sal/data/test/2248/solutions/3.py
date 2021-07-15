import sys
#with open(filename, 'r') as f:
with sys.stdin as f:
    for i, line in enumerate(f):
        if i == 0:
            N, M = line.split(' ')
            N, M = int(N), int(M)
            graph = [[] for _ in range(N)] # [[]] * N not working, no deepcopy
        else:
            fromVertex, toVertex = line.split(' ')
            fromVertex, toVertex = int(fromVertex)-1, int(toVertex)-1
            graph[fromVertex].append(toVertex)
            graph[toVertex].append(fromVertex)


# code is too slow, O(N^3)
#~ INFINITY = 9999999
#~ from queue import Queue
#~ def bfs(start_node, graph):
    #~ N = len(graph)
    #~ distances = [INFINITY for _ in range(N)]
    #~ distances[start_node] = 0
    #~ nodes_queue = Queue()
    #~ nodes_queue.put(start_node)
    #~ while not nodes_queue.empty():
        #~ node = nodes_queue.get()
        #~ for neigh in graph[node]:
            #~ if distances[neigh] == INFINITY:
                #~ # not yet visited
                #~ distances[neigh] = distances[node] + 1
                #~ nodes_queue.put(neigh)
        
    #~ return distances
    
# use tree structure
from queue import Queue
def farthest_node_distance(start_node, graph):
    """ returns farthest node from start node and its distance """
    N = len(graph)
    visited = [False for _ in range(N)]
    distances = [-1 for _ in range(N)]
    visited[start_node] = True
    distances[start_node] = 0
    nodes_queue = Queue()
    nodes_queue.put(start_node)
    while not nodes_queue.empty():
        node = nodes_queue.get()
        #print("Taking {}: {}".format(node, distances[node]))
        for neigh in graph[node]:
            if not visited[neigh]:
                #print("Found {}".format(neigh))
                visited[neigh] = True
                distances[neigh] = distances[node] + 1
                nodes_queue.put(neigh)
                #print("{}: {}".format(neigh, distances[neigh]))
    return node, distances[node]

u, dist_u = farthest_node_distance(0, graph)
#print("Done")
v, dist_uv = farthest_node_distance(u, graph)
print(dist_uv)
#print("u: {}, {}".format(u, dist_u))
#print("v: {}, {}".format(v, dist_uv))

