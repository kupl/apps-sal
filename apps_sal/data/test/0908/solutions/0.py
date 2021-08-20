n = int(input())
c = list(map(int, input().split(' ')))
nodes = dict()
nodes[''] = 0
depth = 0
while depth < n:
    new_nodes = dict()
    s = input()
    for node in nodes.keys():
        if s >= node:
            if s in new_nodes:
                new_nodes[s] = min(new_nodes[s], nodes[node])
            else:
                new_nodes[s] = nodes[node]
        if s[::-1] >= node:
            if s[::-1] in new_nodes:
                new_nodes[s[::-1]] = min(new_nodes[s[::-1]], nodes[node] + c[depth])
            else:
                new_nodes[s[::-1]] = nodes[node] + c[depth]
    nodes = new_nodes
    depth += 1
if len(nodes) > 0:
    print(min(nodes.values()))
else:
    print(-1)
