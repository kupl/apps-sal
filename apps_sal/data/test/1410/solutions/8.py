import itertools
import math


def main():
    tree = dict()
    n = int(input())
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    costs = [(c1[i], c2[i], c3[i]) for i in range(len(c1))]
    no_sol = False
    for i in range(n - 1):
        a, b = list(map(int, input().split()))
        if a not in tree:
            tree[a] = [b]
        else:
            tree[a].append(b)
        if b not in tree:
            tree[b] = [a]
        else:
            tree[b].append(a)
        if len(tree[a]) > 2:
            no_sol = True
        if len(tree[b]) > 2:
            no_sol = True

    if no_sol:
        print(-1)
        return

    for node in list(tree.keys()):
        if len(tree[node]) == 1:
            start = node
            break

    lst = [start]
    visited = [0] * (n + 1)
    visited[node] = 1
    node = start
    while len(lst) < n:
        for i in tree[node]:
            if visited[i] == 0:
                visited[i] = 1
                lst.append(i)
                node = i
                break

    permutations = list(itertools.permutations([1, 2, 3], 3))
    cost = [0] * len(permutations)

    idx_permut = -1
    min_sum = math.inf
    for permut in range(len(permutations)):
        cost_sum = 0
        for i in range(len(lst)):
            list_cost = costs[lst[i] - 1]
            cost_sum += list_cost[permutations[permut][i % 3] - 1]
        cost[permut] = cost_sum
        if cost_sum < min_sum:
            min_sum = cost_sum
            idx_permut = permut

    d_sol = [0] * (len(lst) + 1)
    idx = 0
    my_perm = permutations[idx_permut]
    for i in lst:
        d_sol[i] = my_perm[idx % 3]
        idx += 1

    solution = d_sol[1:]

    print(min_sum)
    print(" ".join(map(str, solution)))


def __starting_point():
    main()


__starting_point()
