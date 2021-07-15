def intline():
    return [int(s) for s in input().split()]

# number of vertices in tree
# acceptable number of consecutive cat vertices
n, m = intline()

# cat vertices
a = [0] + intline()

# read tree structure
tree = {}
for i in range(n - 1):
    x, y = intline()

    if x not in tree:
        tree[x] = []
    if y not in tree:
        tree[y] = []

    tree[x].append(y)
    tree[y].append(x)

# dfs from root down to every leaf
seen = [False] * (n + 1)
work = [(1, 0)]
paths = 0
while work:
    cur, run = work.pop()

    # already visited, no more leaves down here
    if seen[cur]:
        continue
    seen[cur] = True

    # calculate the current run
    if a[cur]:
        run += 1
    else:
        run = 0

    # more than the allowed number of consecutive cat vertices
    if run > m:
        continue

    # leaf, only has an edge to the parent
    if len(tree[cur]) == 1 and cur != 1:
        paths += 1
        continue

    for neighbour in tree[cur]:
        work.append([neighbour, run])

print(paths)

