
from collections import defaultdict


def _vertex(lit):
    if lit > 0:
        return 2 * (lit - 1)
    else:
        return 2 * (-lit - 1) + 1


def tarjan(graph):
    n = len(graph)
    dfs_num = [None] * n
    dfs_min = [n] * n
    waiting = []
    waits = [False] * n
    sccp = []
    dfs_time = 0
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                if times_seen[node] == 0:
                    dfs_num[node] = dfs_time
                    dfs_min[node] = dfs_time
                    dfs_time += 1
                    waiting.append(node)
                    waits[node] = True
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    dfs_min[node] = dfs_num[node]
                    for child in children:
                        if waits[child] and dfs_min[child] < dfs_min[node]:
                            dfs_min[node] = dfs_min[child]
                    if dfs_min[node] == dfs_num[node]:
                        component = []
                        while True:
                            u = waiting.pop()
                            waits[u] = False
                            component.append(u)
                            if u == node:
                                break
                        sccp.append(component)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        times_seen[child] = 0
                        to_visit.append(child)
    return sccp


def two_sat(formula):
    n = max(abs(clause[p]) for p in (0, 1) for clause in formula)
    graph = [[] for node in range(2 * n)]
    for x, y in formula:
        graph[_vertex(-x)].append(_vertex(y))
        graph[_vertex(-y)].append(_vertex(x))
    sccp = tarjan(graph)
    comp_id = [None] * (2 * n)
    for component in sccp:
        rep = min(component)
        for vtx in component:
            comp_id[vtx] = rep
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            return "NO"
    return "YES"


n, m = [int(x) for x in input().split()]
doors_status = [int(x) for x in input().split()]
switches = [list(map(int, input().split())) for _ in range(m)]

switches_of = defaultdict(list)
for switch in range(1, m + 1):
    for door in switches[switch - 1][1:]:
        switches_of[door].append(switch)

LOCKED = 0
UNLOCKED = 1
formula = []
for door in range(1, n + 1):
    s1, s2 = switches_of[door]
    if doors_status[door - 1] == LOCKED:
        formula.append((s1, s2))
        formula.append((-s1, -s2))
    else:
        formula.append((s1, -s2))
        formula.append((-s1, s2))

print(two_sat(formula))
