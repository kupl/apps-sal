import sys
from heapq import heappush, heappop
from collections import Counter, defaultdict

# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, line.split())) for line in sys.stdin)

def insert(pq, value, entry_finder, push_id):
    entry = [value, push_id]
    entry_finder[push_id] = entry
    heappush(pq, entry)    

def remove(entry_finder, push_id):
    entry = entry_finder.pop(push_id)
    entry[-1] = -1
    
def extract_min(pq, entry_finder):
    while pq:
        value, push_id = heappop(pq)
        if push_id > 0:
            del entry_finder[push_id]
            return (push_id, value)
    return (-1, '*')

t, = next(reader)
for test in range(t):
    n, = next(reader)
    pq = []
    entry_finder = {}
    triangle = [tuple(next(reader)) for _ in range(n-2)]
    deg = Counter()
    v_tri = defaultdict(list)
    used = set()
    for i, tri in enumerate(triangle):
        for v in tri:
            deg[v] += 1
            v_tri[v].append(i)
    for v, value in list(deg.items()):
        insert(pq, value, entry_finder, push_id=v)
    g = [set() for _ in range(n+1)]
    ansQ = []
    for _ in range(n-2):
        v, value = extract_min(pq, entry_finder)
        while True:
            i = v_tri[v].pop()
            if i not in used:
                break
        used.add(i)
        ansQ.append(i+1)
        tri = triangle[i]
        tos = [to for to in tri if to != v]
        for to in tos:
            if to in g[v]:
                g[v].remove(to)
                g[to].remove(v)
            else:
                g[v].add(to)
                g[to].add(v)
            deg[to] -= 1
            remove(entry_finder, push_id=to)
            insert(pq, deg[to], entry_finder, push_id=to)
        to1, to2 = tos
        if to1 in g[to2]:
            g[to1].remove(to2)
            g[to2].remove(to1)
        else:
            g[to1].add(to2)
            g[to2].add(to1)
    ansP = []
    visited = [False] * (n+1)
    s = 1
    stack = [s]
#     print(g)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            ansP.append(v)
            for to in g[v]:
                stack.append(to)
    print(*ansP)
    print(*ansQ)

# inf.close()

