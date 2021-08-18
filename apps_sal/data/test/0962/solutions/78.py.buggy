N, M = map(int, input().split())
tree = dict(zip(range(1, N + 1), [[] for i in range(N)]))
for i in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)


is_visited = [False] * (N + 1)
num_visited = 0


def find_cycle(d):
    nonlocal is_visited
    nonlocal num_visited
    cycle = []
    l = 1001
    while d:
        node = d[-1]
        if tree[node]:
            child = tree[node].pop()
            if not is_visited[child]:
                is_visited[child] = True
                num_visited += 1
            if child in cycle and node in cycle:
                idn = cycle.index(node)
                idc = cycle.index(child)
                cycle = cycle[:idn + 1] + cycle[idc:]
                l = len(cycle)
            if child in d:
                idx = d.index(child)
                if len(d) - idx < l:
                    cycle = d[idx:]
                    l = len(cycle)
            else:
                d.append(child)
        else:
            d.pop()
    return cycle


is_visited[0] = True
num_visited += 1
i = 1
while num_visited < N + 1:
    while is_visited[i]:
        i += 1
    d = [i]
    is_visited[i] = True
    num_visited += 1
    cycle = find_cycle(d)
    if cycle:
        print(len(cycle))
        print(*cycle, sep='\n')
        return

print(-1)
