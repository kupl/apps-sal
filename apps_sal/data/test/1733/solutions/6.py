import sys
from collections import deque


def get_roots_direct_children(q, roots_direct_children, visited, edges):
    while q:
        root = q.popleft()
        visited[root] = True
        root_direct_children = list()
        for vertice in edges[root]:
            if not visited[vertice]:
                q.appendleft(vertice)
                visited[vertice] = True
                root_direct_children.append(vertice)
        roots_direct_children.append((root, root_direct_children))


def get_cnt(cnt, roots_direct_children):
    while roots_direct_children:
        cur_tuple = roots_direct_children.pop()
        root = cur_tuple[0]
        direct_children = cur_tuple[1]
        for direct_child in direct_children:
            cnt[root] += cnt[direct_child]


def solve():
    input = sys.stdin.readline
    (n, x, y) = map(int, input().split())
    edges = {vertice: list() for vertice in range(1, n + 1)}
    for i in range(n - 1):
        uv = input().split()
        u = int(uv[0])
        v = int(uv[1])
        edges[u].append(v)
        edges[v].append(u)
    cnt = [1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    q = deque()
    q.append(x)
    roots_direct_children = list()
    get_roots_direct_children(q, roots_direct_children, visited, edges)
    get_cnt(cnt, roots_direct_children)
    cnt_y = cnt[y]
    q = deque()
    q.append(y)
    roots_direct_children = list()
    cnt = [1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    get_roots_direct_children(q, roots_direct_children, visited, edges)
    get_cnt(cnt, roots_direct_children)
    cnt_x = cnt[x]
    total = n * (n - 1)
    not_ok_routes = cnt_x * cnt_y
    result = total - not_ok_routes
    print(result)


solve()
