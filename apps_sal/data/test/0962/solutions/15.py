def dfs(N, AB):
    status = [-1] * N
    for i in range(N):
        if status[i] == 1:
            continue
        stack = [i]
        status[i] = 0
        while stack:
            v = stack[-1]
            if AB[v]:
                n = AB[v].pop()
                if status[n] == -1:
                    stack.append(n)
                    status[n] = 0
                elif status[n] == 0:
                    idx = stack.index(n)
                    cycle = stack[idx:]

                    return cycle
            else:
                status[v] = 1
                stack.pop()

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


N, M = [int(i) for i in input().split()]

AB = [[] for _ in range(N)]
for _ in range(M):
    A, B = [int(i) - 1 for i in input().split()]
    AB[A].append(B)

cycle = dfs(N, AB)
if not cycle:
    print(-1)
else:
    cycle = find_smaller_cycle(cycle, AB)

    print(len(cycle))
    for v in cycle:
        print(v + 1)
