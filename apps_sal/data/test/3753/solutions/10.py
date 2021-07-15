from sys import stdin
from collections import defaultdict
n, m = list(map(int, input().split()))

if n == 1 or m == 1:
    if '#' in stdin.read():
        print(0)
    else:
        print(1)
    return

graph = []
for i in range(n):
    graph.append(input())

def dfs(visited):
    reachable = []
    stack = []
    stack.append((0, 0))
    
    while stack:
        node_r, node_c = stack.pop()
        if not visited[node_r][node_c]:
            visited[node_r][node_c] = True
            reachable.append((node_r, node_c))
            if node_r + 1 < n and not visited[node_r + 1][node_c] and graph[node_r + 1][node_c] != '#':
                stack.append((node_r + 1, node_c))
            if node_c + 1 < m and not visited[node_r][node_c + 1] and graph[node_r][node_c + 1] != '#':
                stack.append((node_r, node_c + 1))
            if node_r == n - 1 and node_c == m - 1:
                break
    
    return reachable

'''           
def dfs_reverse():
    visited = [[False for j in range(m)] for i in range(n)]
    reachable = []
    stack = []
    stack.append((n - 1, m - 1))

    while stack:
        node_r, node_c = stack.pop()
        if not visited[node_r][node_c]:
            visited[node_r][node_c] = True
            reachable.append((node_r, node_c))
            if node_r - 1 >= 0 and not visited[node_r - 1][node_c] and graph[node_r - 1][node_c] != '#':
                stack.append((node_r - 1, node_c))
            if node_c - 1 >= 0 and not visited[node_r][node_c - 1] and graph[node_r][node_c - 1] != '#':
                stack.append((node_r, node_c - 1))
    
    return reachable
'''

visited = [[False for j in range(m)] for i in range(n)]
dfs(visited)

if not visited[n - 1][m - 1]:
    print(0)
else:
    visited[0][0] = False
    visited[n - 1][m - 1] = False
    dfs(visited)
    if visited[n - 1][m - 1]:
        print(2)
    else:
        print(1)

