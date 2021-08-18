def solve():
    order = list
    length = len
    unique = set
    nodes, edges, distinct = order(map(int, input().split(" ")))
    govt = {x - 1: 1 for x in order(map(int, input().split(" ")))}
    connections = {}

    for _ in range(edges):
        x, y = order(map(int, input().split(" ")))

        if x - 1 not in connections:
            connections[x - 1] = [y - 1]
        else:
            connections[x - 1].append(y - 1)

        if y - 1 not in connections:
            connections[y - 1] = [x - 1]
        else:
            connections[y - 1].append(x - 1)

    discovered = {}
    cycles = {m: [] for m in ["G", "N"]}
    for i in range(nodes):
        is_govt = False if i not in govt else True

        if i in discovered:
            continue

        cycle = [i]
        if i not in connections:
            discovered[i] = 1
            if is_govt:
                cycles["G"].append(cycle)
            else:
                cycles["N"].append(cycle)
            continue

        path = connections[i]
        while length(path) > 0:
            node = path.pop(0)

            if node in discovered:
                continue
            discovered[node] = 1

            if node in govt:
                is_govt = True

            path = connections[node] + path
            cycle.append(node)

        if is_govt:
            cycles["G"].append(order(unique(cycle)))
        else:
            cycles["N"].append(order(unique(cycle)))

    ordered_cycles = sorted(cycles["G"], key=len)

    highest = length(ordered_cycles[-1])
    ordered_cycles.pop(length(ordered_cycles) - 1)
    for cycle in cycles["N"]:
        highest += length(cycle)

    total = highest * (highest - 1) // 2
    for j in ordered_cycles:
        total += length(j) * (length(j) - 1) // 2

    print(total - edges)


solve()
