import sys
input = sys.stdin.readline
from scipy.sparse.csgraph import floyd_warshall
      
n,m,l = map(int,input().split())
edge = [[0]*n for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    edge[a-1][b-1] = c
    edge[b-1][a-1] = c

edge = floyd_warshall(edge)
    
for i in range(n):
    for j in range(n):
        if edge[i][j]<=l:
            edge[i][j] = 1
        else:
            edge[i][j] = 0
                
edge = floyd_warshall(edge)

q = int(input())
for i in range(q):
    s,t = map(int,input().split())
    if edge[s-1][t-1] == float("inf"):
        print(-1)
    else:
        print(int(edge[s-1][t-1] - 1))
