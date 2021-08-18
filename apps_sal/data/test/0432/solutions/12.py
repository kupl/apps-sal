n = input()
a = list(map(int, input().split()))
a_next = list(map(int, input().split()))
for i in range(len(a_next)):
    a_next[i] -= 1

cycles = []
check = [0] * len(a)


def dfs(v):
    path = []
    s = []

    check[v] = 1
    path.append(v)
    s.append(v)

    while s:
        next_v = a_next[s[-1]]

        if check[next_v] == 0:
            check[next_v] = 1
            path.append(next_v)
            s.append(next_v)
        else:
            if check[next_v] == 1:
                cycle = []
                while path[-1] != next_v:
                    cycle.append(path.pop())
                cycle.append(next_v)
                cycles.append(cycle)
            while s:
                check[s.pop()] = 2


for i in range(len(a)):
    if check[i] == 0:
        dfs(i)

ans = 0
for cycle in cycles:
    min_cost = a[cycle[0]]
    for v in cycle:
        if a[v] < min_cost:
            min_cost = a[v]
    ans += min_cost

print(ans)
