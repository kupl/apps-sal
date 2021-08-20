from sys import stdin
input = stdin.readline
(n, m) = [int(i) for i in input().split()]
edges = [[[0 for i in range(n)], 0] for i in range(n + 1)]
edges_2 = [[0, 0] for i in range(m)]
for i in range(m):
    (v, w) = [int(i) for i in input().split()]
    edges[v][0][edges[v][1]] = w
    edges[v][1] += 1
    edges_2[i] = [v, w]
is_one = True
for i in range(1, n + 1):
    visited = [0 for i in range(n)]
    visited[0] = i
    num_visited = 1
    act = 0
    while act <= num_visited - 1:
        for j in range(edges[visited[act]][1]):
            if edges[visited[act]][0][j] == i:
                is_one = False
            elif edges[visited[act]][0][j] not in visited:
                visited[num_visited] = edges[visited[act]][0][j]
                num_visited += 1
        act += 1
if is_one:
    print(1)
    for i in range(m - 1):
        print('1', end=' ')
    print(1)
else:
    print(2)
    for i in range(m - 1):
        if edges_2[i][0] < edges_2[i][1]:
            print('1', end=' ')
        else:
            print('2', end=' ')
    if edges_2[-1][0] < edges_2[-1][1]:
        print('1')
    else:
        print('2')
