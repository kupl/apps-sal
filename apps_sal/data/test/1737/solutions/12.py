def read_pack():
    name, ver = input().strip().split()
    return (name, int(ver))

n = int(input())
deps = dict()
for i in range(n):
    pack = read_pack()
    if not i:
        root = pack
    dep_n = int(input())
    deps[pack] = [read_pack() for _ in range(dep_n)]
    if i != n - 1:
        input()

queue = [(root, 0)]
taken = {root[0]: (root[1], 0)}
for pack, level in queue:
    # pack_deps = sorted(deps[pack], key=lambda x: x[1], reverse=True)
    for dep in deps[pack]:
        if dep[0] not in taken:
            taken[dep[0]] = (dep[1], level + 1)
            queue.append((dep, level + 1))
        elif taken[dep[0]][1] == level + 1 and taken[dep[0]][0] < dep[1]:
            index = queue.index(((dep[0], taken[dep[0]][0]), level + 1))
            taken[dep[0]] = (dep[1], level + 1)
            queue[index] = (dep, level + 1)

del taken[root[0]]

print(len(taken))

for d in sorted(taken):
    print(d, taken[d][0])
