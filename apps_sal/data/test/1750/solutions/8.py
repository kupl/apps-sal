from collections import deque

n = int(input())
g = []
visited = []
color = []
max_child_color = []
parent = []

def initialize():
    for i in range(n+10):
        g.append([])
        visited.append(False)
        color.append(0)
        max_child_color.append(0)
        parent.append(0)
    for i in range(n-1):
        u, v = map(int, input().split())
        g[u] += [v]
        g[v] += [u]
    # print(g)

def get_color(u):
    for i in range(max_child_color[u]+1, n+1):
        if i != color[parent[u]] and i != color[u]:
            max_child_color[u] = i
            # print(f'Setting max child color of node = {u} to color {i}')
            return i

def bfs(start):
    visited[start] = True
    color[start] = 1
    q = deque()
    q.append(start)
    while q:
        u = q.popleft()
        for v in g[u]:
            parent[v] = u
            if not visited[v]:
                visited[v] = True
                color[v] = get_color(u)
                q.append(v)

def __starting_point():
    initialize()
    bfs(1)
    print(max(color))
    c_string = ""
    for i in range(1, n+1):
        c_string += str(color[i]) + " "
    print(c_string)
__starting_point()
