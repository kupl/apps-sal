import sys
input = sys.stdin.readline


def topological_sort(tree: list, root) -> list:
    n = len(tree)
    visited = [False] * n
    visited[root] = True
    tp_sorted = [root]
    stack = [root]
    while stack:
        v = stack.pop()
        for nxt_v in tree[v]:
            if visited[nxt_v]:
                continue
            visited[nxt_v] = True
            stack.append(nxt_v)
            tp_sorted.append(nxt_v)
    return tp_sorted


def get_par(tree: list, root: int) -> list:
    n = len(tree)
    visited = [False] * n
    visited[root] = True
    par = [-1] * n
    stack = [root]
    while stack:
        v = stack.pop()
        for nxt_v in tree[v]:
            if visited[nxt_v]:
                continue
            visited[nxt_v] = True
            stack.append(nxt_v)
            par[nxt_v] = v
    return par


t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    p = list(map(int, input().split()))
    h = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    tree = [[] for i in range(n)]
    for (a, b) in edges:
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)
    root = 0
    tp_sort = topological_sort(tree, root)
    par = get_par(tree, root)
    cnts = [[0, 0] for i in range(n)]
    flag = True
    for v in tp_sort[::-1]:
        (good, bad) = (0, 0)
        for nxt_v in tree[v]:
            if nxt_v == par[v]:
                continue
            else:
                good += cnts[nxt_v][0]
                bad += cnts[nxt_v][1]
        sum_p = good + bad + p[v]
        if (sum_p + h[v]) % 2 != 0:
            flag = False
            break
        g = (sum_p + h[v]) // 2
        b = (sum_p - h[v]) // 2
        inc_g = g - good
        if 0 <= inc_g <= p[v] + bad:
            cnts[v] = (g, b)
            continue
        else:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
