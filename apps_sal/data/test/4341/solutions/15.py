def go():
    (n, m) = (int(i) for i in input().split(' '))
    graph = {}
    for _ in range(m):
        (a, b) = (int(i) for i in input().split(' '))
        graph.setdefault(a, [])
        graph.setdefault(b, [])
        graph[a].append(b)
        graph[b].append(a)
    output = 0
    cands = set((i for i in graph if len(graph[i]) == 2))
    while cands:
        c = cands.pop()
        (r, l) = graph[c]
        while l in cands:
            cands.remove(l)
            (c1, c2) = graph[l]
            if c1 in cands:
                l = c1
            elif c2 in cands:
                l = c2
            else:
                break
            if l == r:
                output += 1
    return output


print(go())
