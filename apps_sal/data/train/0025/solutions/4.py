import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    counts = [0] * n
    triangles = [set() for _ in range(n)]
    assign_order = {}
    for i in range(n - 2):
        a, b, c = [x - 1 for x in list(map(int, input().split()))]
        t = (a, b, c)
        assign_order[t] = i
        for x in t:
            counts[x] += 1
            triangles[x].add(t)

    not_edges = set()
    edges = set()
    order = []
    que = [i for i in range(n) if counts[i] == 1]
    index = 0
    while index < n - 2:
        curr = que[index]
        tt = triangles[curr].pop()  # should remain one
        order.append(assign_order[tt])
        t = set(tt)
        t.remove(curr)
        a, b = t.pop(), t.pop()
        for e in (curr, a), (curr, b):
            if e not in not_edges:
                edges.add(e)
        if index < n - 3:
            not_edges.add((a, b))
            not_edges.add((b, a))
        else:
            if (a, b) not in not_edges:
                edges.add((a, b))

        for x in a, b:
            counts[x] -= 1
            if counts[x] == 1:
                que.append(x)
            triangles[x].remove(tt)
        index += 1

    e = [[] for _ in range(n)]
    for a, b in edges:
        e[a].append(b)
        e[b].append(a)

    visited = [False] * n
    a = 0
    answer = []
    for i in range(n):
        visited[a] = True
        answer.append(a)
        for b in e[a]:
            if not visited[b]:
                a = b
                break

    print(' '.join(map(str, [x + 1 for x in answer])))
    print(' '.join(map(str, [x + 1 for x in order])))
