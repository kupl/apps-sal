# -------------------------SOLVE STACK OVERFFLOW WHILE DFS
# input
n = input()
a = list(map(int, input().split()))  # costs of each room
a_next = list(map(int, input().split()))  # a_next[i] : the next room of ith room
for i in range(len(a_next)):
    a_next[i] -= 1

cycles = []  # list of cycles
check = [0] * len(a)  # check array (0:unchecked, 1:visited, 2:belongs to a cycle)

# dfs function. make cycles along the way


def dfs(v):
    path = []  # path of dfs
    s = []  # dfs stack

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
            if check[next_v] == 1:  # a new cycle has been found
                cycle = []
                while path[-1] != next_v:
                    cycle.append(path.pop())
                cycle.append(next_v)
                cycles.append(cycle)
            # empty the stack
            while s:
                check[s.pop()] = 2


# make a list of cycles
for i in range(len(a)):
    if check[i] == 0:
        dfs(i)

# add up all minimum costs for each cycle
ans = 0  # answer
for cycle in cycles:
    min_cost = a[cycle[0]]
    for v in cycle:
        if a[v] < min_cost:
            min_cost = a[v]
    ans += min_cost

# print answer
print(ans)
