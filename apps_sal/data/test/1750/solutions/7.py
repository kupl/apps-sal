import collections
def doit():
    N = int(input())
    graph = dict()
    for n in range(N) :
        graph[n] = list()

    for n in range(N - 1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    msize = 0
    for k in graph:
        msize = max(msize, len(graph[k]))
    print(msize+1)

    root = 0

    colors = [0 for x in range(N)]
    colors[root] = 1
    parents = [0 for x in range(N)]
    parents[root] = root

    def colorgenerator(c1, c2):
        colorindex = 0
        while colorindex < msize + 1:
            colorindex += 1
            if colorindex == c1 or colorindex == c2:
                continue
            yield colorindex

    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        color = colorgenerator(colors[vertex], colors[parents[vertex]])
        for neighbour in graph[vertex]:
            if neighbour == parents[vertex]:
                continue

            parents[neighbour] = vertex
            colors[neighbour] = next(color)
            queue.append(neighbour)
    print(" ".join(map(str, colors)))

doit()
