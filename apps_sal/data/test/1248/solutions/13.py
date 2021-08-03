adj = [[0] * 3 for x in range(3)]
a, b, c = list(map(int, input().split()))
adj[0][1] = adj[1][0] = a
adj[0][2] = adj[2][0] = b
adj[1][2] = adj[2][1] = c
for k in range(3):
    for i in range(3):
        for j in range(3):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
print(adj[0][1] + adj[1][2] + adj[2][0])
