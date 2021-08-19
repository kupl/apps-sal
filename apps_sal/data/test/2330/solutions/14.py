def run_testcase():
    [n, m] = [int(x) for x in input().split()]
    ns = [int(x) for x in input().split()]
    if n == 2:
        print(-1)
        return
    if m < n:
        print(-1)
        return
    sum_ns = sum(ns)
    cost = 2 * sum_ns
    rest_m = m - n
    sorted_ns = list(sorted(ns))
    cheapest_edge = sorted_ns[0] + sorted_ns[1]
    cost += cheapest_edge * rest_m
    edges = [None] * m
    edges[0] = (1, n)
    for i in range(1, n):
        edges[i] = (i, i + 1)
    for i in range(rest_m):
        edges[n + i] = (sorted_ns[0], sorted_ns[1])
    print(cost)
    for edge in edges:
        print(edge[0], edge[1])


testcase_count = int(input())
for i in range(testcase_count):
    run_testcase()
