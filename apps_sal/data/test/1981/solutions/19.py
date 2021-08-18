def intline():
    return [int(s) for s in input().split()]


n, m = intline()

a = [0] + intline()

tree = {}
for i in range(n - 1):
    x, y = intline()

    if x not in tree:
        tree[x] = []
    if y not in tree:
        tree[y] = []

    tree[x].append(y)
    tree[y].append(x)

seen = [False] * (n + 1)
work = [(1, 0)]
paths = 0
while work:
    cur, run = work.pop()

    if seen[cur]:
        continue
    seen[cur] = True

    if a[cur]:
        run += 1
    else:
        run = 0

    if run > m:
        continue

    if len(tree[cur]) == 1 and cur != 1:
        paths += 1
        continue

    for neighbour in tree[cur]:
        work.append([neighbour, run])

print(paths)
