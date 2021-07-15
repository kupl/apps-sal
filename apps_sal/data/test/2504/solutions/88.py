from scipy.sparse.csgraph import floyd_warshall

N,M,L = list(map(int, input().split()))

edges = [[0] * N for _ in range(N)]

for _ in range(M):
    A,B,C = list(map(int, input().split()))
    edges[A-1][B-1] = C
    edges[B-1][A-1] = C

Q = int(input())
queries = []

for _ in range(Q):
    queries.append(list(map(int,input().split())))

# use flord warshall to find min path between all towns
edges = floyd_warshall(edges)

# if the two towns can be travelled to on one tank, add to our fuel graph with distance 1
for i in range(N):
    for j in range(N):
        if edges[i][j] <= L:
            edges[i][j] = 1
        else:
            edges[i][j] = 0

# use flord warshall to find min number of fuel tanks to travel between two towns
edges = floyd_warshall(edges)

for query in queries:
    s = query[0] - 1
    t = query[1] - 1
    num_tanks = edges[s][t] - 1
    if num_tanks != float('inf'):
        print((int(num_tanks)))
    else:
        print("-1")

