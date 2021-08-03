import collections


def doit():
    # rows = [[] for y in range(M)]
    rows = dict()

    N = int(input())
    graph = dict()
    for n in range(N):
        graph[n] = list()

    for n in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    msize = 0
    for k in graph:
        msize = max(msize, len(graph[k]))
    print(msize + 1)

    root = 0
    colors = [0 for x in range(N)]
    colors[root] = 1
    parents = [0 for x in range(N)]
    parents[root] = root

    def color(c1, c2):
        colorindex = 0
        while colorindex < msize + 1:
            colorindex += 1
            if colorindex == c1 or colorindex == c2:
                continue
            yield colorindex

    # visited = set()
    # visited.add(root)
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        # newcolors = [c for c in range(1, msize+2) if c != colors[vertex] and c != colors[parents[vertex]] ]
        # newcolors = filter(lambda c: c != colors[vertex] and c != colors[parents[vertex]], range(1, msize+2))
        #
        # print(f'newcolors={newcolors}')
        colorgen = color(colors[vertex], colors[parents[vertex]])
        for neighbour in graph[vertex]:
            if neighbour == parents[vertex]:
                continue
            parents[neighbour] = vertex
            colors[neighbour] = next(colorgen)
            # visited.add(neighbour)
            queue.append(neighbour)
    print(" ".join(map(str, colors)))


doit()
