3

import sys

"""
4 6
<><>
v^v^v^
"""

def num_of_accessible(g, node):
    q = [node]
    seen = set([node])
    while len(q) > 0:
        v = q.pop()
        for u in g[v]:
            if u in seen:
                continue
            seen.add(u)
            q.append(u)
    return len(seen)

def __starting_point():
    n, m = list(map(int, sys.stdin.readline().split()))
    horiz = sys.stdin.readline().strip()
    vert = sys.stdin.readline().strip()
    
    # Graph
    g = {(i, j): [] for i in range(n) for j in range(m)}
    for i, h in enumerate(horiz):
        if h == '<':
            for j in range(m-1):
                g[(i, j+1)].append((i, j))
        else:
            for j in range(m-1):
                g[(i, j)].append((i, j+1))
    for j, v in enumerate(vert):
        if v == 'v':
            for i in range(n-1):
                g[(i, j)].append((i+1, j))
        else:
            for i in range(n-1):
                g[(i+1, j)].append((i, j))
        
    conn = True
    for node in g:
        if num_of_accessible(g, node) < n*m:
            conn = False
            break
    
    print('YES' if conn else 'NO')

__starting_point()
