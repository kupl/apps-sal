import sys
#with open(filename, 'r') as f:
with sys.stdin as f:
    for i, line in enumerate(f):
        if i == 0:
            N = int(line)
            graph = [[] for _ in range(N)] # [[]] * N not working, no deepcopy
        else:
            fromVertex, toVertex = line.split(' ')
            fromVertex, toVertex = int(fromVertex)-1, int(toVertex)-1
            graph[fromVertex].append(toVertex)
            graph[toVertex].append(fromVertex)

nb_paths = 0
for i in range(N):
    degr = len(graph[i])
    nb_paths += int((degr*(degr-1))/2)
print(nb_paths)
