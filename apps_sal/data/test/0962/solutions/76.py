def find_cycle(N, AB):
    for c in range(N):
        stack = [(c, [])]
        while stack:
            (curr, visited) = stack.pop()
            if curr in visited:
                return visited
            else:
                for i in AB[curr]:
                    stack.append((i, visited + [curr]))
    return False


def find_smaller_cycle(cycle, AB):
    i = 0
    while i < len(cycle):
        v = cycle[i]
        if AB[v]:
            n = AB[v].pop()
            if n in cycle:
                r = cycle.index(n)
                if i < r:
                    cycle = cycle[:i + 1] + cycle[r:]
                else:
                    cycle = cycle[r:i + 1]
                i = cycle.index(v)
        else:
            i += 1
    return cycle


(N, M) = [int(i) for i in input().split()]
AB = [[] for _ in range(N)]
for _ in range(M):
    (A, B) = [int(i) - 1 for i in input().split()]
    AB[A].append(B)
cycle = find_cycle(N, AB)
if not cycle:
    print(-1)
else:
    cycle = find_smaller_cycle(cycle, AB)
    print(len(cycle))
    for v in cycle:
        print(v + 1)
