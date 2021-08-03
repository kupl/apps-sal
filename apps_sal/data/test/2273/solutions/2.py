from collections import defaultdict, deque


def threeSets(vs, es, d):
    sets = [3] * vs

    s1 = 0
    dist = [float('inf')] * vs
    sets[s1] = 1
    dist[s1] = 0
    queue = deque([s1])
    while queue:
        v1 = queue.pop()
        for v2 in d[v1]:
            if dist[v2] > dist[v1] + 1:
                dist[v2] = dist[v1] + 1
                queue.appendleft(v2)

    for i in range(vs):
        if dist[i] > 2:
            return [-1]
        elif dist[i] == 2:
            sets[i] = 1

    try:
        s2 = sets.index(3)
    except:
        return [-1]

    dist = [float('inf')] * vs
    sets[s2] = 2
    dist[s2] = 0
    queue = deque([s2])
    while queue:
        v1 = queue.pop()
        for v2 in d[v1]:
            if dist[v2] > dist[v1] + 1:
                dist[v2] = dist[v1] + 1
                queue.appendleft(v2)

    for i in range(vs):
        if dist[i] > 2:
            return [-1]
        elif dist[i] == 2:
            if sets[i] == 1:
                return [-1]
            else:
                sets[i] = 2

    VS = [set() for i in range(3)]
    for i in range(vs):
        g = sets[i] - 1
        VS[g].add(i)
    for V in VS:
        if not len(V):
            return [-1]

    for v1 in VS[0]:
        for v2 in VS[1]:
            if v2 not in d[v1]:
                return [-1]

        for v2 in VS[2]:
            if v2 not in d[v1]:
                return [-1]

    for v1 in VS[1]:
        for v2 in VS[2]:
            if v2 not in d[v1]:
                return [-1]

    valid_es = len(VS[0]) * len(VS[1]) + len(VS[0]) * len(VS[2]) + len(VS[1]) * len(VS[2])
    return sets if es == valid_es else [-1]


d = defaultdict(set)

vs, es = list(map(int, input().split()))
for _ in range(es):
    v1, v2 = list(map(int, input().split()))
    v1 -= 1
    v2 -= 1
    d[v1].add(v2)
    d[v2].add(v1)

print(*threeSets(vs, es, d))
