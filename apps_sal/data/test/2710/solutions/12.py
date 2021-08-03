from collections import deque
from sys import stdin, stdout

MAX_SOLDIERS = 200000


def solve():
    n, m = [int(_) for _ in stdin.readline().rstrip().split()]
    all_lines = stdin.readlines()
    start_vals = [int(_) for _ in all_lines[0].split()]
    end_vals = [int(_) for _ in all_lines[1].split()]
    if sum(start_vals) != sum(end_vals):
        stdout.write('NO\n')
        return
    graph = [[0] * (n * 2 + 2) for _ in range(n * 2 + 2)]
    edges = [(_, _) for _ in range(1, n + 1)]
    for i in range(n):
        graph[0][i + 1] = start_vals[i]
        graph[n + i + 1][n * 2 + 2 - 1] = end_vals[i]
        graph[i + 1][n + i + 1] = start_vals[i]
    for index in range(m):
        i, j = [int(_) for _ in all_lines[2 + index].split()]
        graph[i][n + j] = start_vals[i - 1]
        graph[j][n + i] = start_vals[j - 1]
        edges.append((i, j))
    flow = maxflow(graph)
    if flow != sum(start_vals):
        stdout.write('NO\n')
        return
    mat = [[0] * n for _ in range(n)]
    for (i, j) in edges:
        mat[i - 1][j - 1] = start_vals[i - 1] - graph[i][n + j]
        mat[j - 1][i - 1] = start_vals[j - 1] - graph[j][n + i]
    stdout.write('YES\n')
    for i in mat:
        stdout.write(' '.join(str(_) for _ in i))
        stdout.write('\n')


def bfs(graph, parent):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    queue = deque([])
    queue.append(0)
    visited[0] = True
    while queue:
        curr_node = queue.popleft()
        for i in range(num_nodes):
            if graph[curr_node][i] > 0 and (not visited[i]):
                queue.append(i)
                visited[i] = True
                parent[i] = curr_node
                if i == num_nodes - 1:
                    return True
    return visited[num_nodes - 1]


def maxflow(graph):
    num_nodes = len(graph)
    parent = [-1] * num_nodes
    ans = 0
    while bfs(graph, parent):
        curr_flow = MAX_SOLDIERS + 1
        curr_node = num_nodes - 1
        while curr_node != 0:
            curr_flow = min(curr_flow, graph[parent[curr_node]][curr_node])
            curr_node = parent[curr_node]
        ans += curr_flow
        curr_node = num_nodes - 1
        while curr_node != 0:
            par = parent[curr_node]
            graph[par][curr_node] -= curr_flow
            graph[curr_node][par] += curr_flow
            curr_node = par
    return ans


solve()
stdout.close()
