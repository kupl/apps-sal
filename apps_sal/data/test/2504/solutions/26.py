from scipy.sparse.csgraph import dijkstra as di

n,m,l = list(map(int, input().split()))

inf = float('INF')
road = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = list(map(int, input().split()))
    a -= 1
    b -= 1
    road[a][b] = road[b][a] = c

def warshall(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

roads = di(road, n)
# [print(cost) for cost in road]
# print()
costs = [[1 if roads[i][j] <= l and i != j else 0 for j in range(n)] for i in range(n)]
costs = di(costs, n)

# [print(cost) for cost in costs]
q = int(input())
for i in range(q):
    s,t = list(map(int, input().split()))
    
    print((int(costs[s-1][t-1]-1) if costs[s-1][t-1] < inf else -1))

