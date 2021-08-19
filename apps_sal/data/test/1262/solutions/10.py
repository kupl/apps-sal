from collections import deque
from math import inf


def run_testcase():
    n = int(input())
    coords = [None] * (n + 1)
    for i in range(1, n + 1):
        coords[i] = [int(x) for x in input().split()]
    ci = [0] + [int(x) for x in input().split()]
    ki = [0] + [int(x) for x in input().split()]

    def cost(i, j):
        if i == j:
            return 0
        if i > j:
            (i, j) = (j, i)
        if i == 0:
            return ci[j]
        return (abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1])) * (ki[i] + ki[j])
    current_cost = 0
    tree = set([0])
    rest = set(range(1, n + 1))
    included = [True] + [False] * n
    connections = deque()
    connections_to_station = 0
    min_attach_cost = [(0, 0)] + [(cost(0, j), 0) for j in range(1, n + 1)]
    while len(tree) < n + 1:
        min_pair = (0, 0)
        min_cost = inf
        for node in rest:
            if min_attach_cost[node][0] < min_cost:
                min_pair = (min_attach_cost[node][1], node)
                min_cost = min_attach_cost[node][0]
        tree.add(min_pair[1])
        included[min_pair[1]] = True
        current_cost += min_cost
        rest.remove(min_pair[1])
        for node in rest:
            if cost(min_pair[1], node) < min_attach_cost[node][0]:
                min_attach_cost[node] = (cost(min_pair[1], node), min_pair[1])
        min_pair = tuple(sorted(min_pair))
        if min_pair[0] == 0:
            connections.appendleft(min_pair)
            connections_to_station += 1
        else:
            connections.append(min_pair)
    connections_list = list(connections)
    print(current_cost)
    print(connections_to_station)
    print(' '.join([str(x[1]) for x in connections_list[:connections_to_station]]))
    print(len(connections_list) - connections_to_station)
    for i in range(connections_to_station, len(connections_list)):
        print(connections_list[i][0], connections_list[i][1])


run_testcase()
