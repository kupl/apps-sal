(n, m) = list(map(int, input().split()))
order = [[] for i in range(n + 1)]
id_perf_map = [-1 for i in range(m + 1)]
for i in range(1, m + 1):
    (p, y) = list(map(int, input().split()))
    id_perf_map[i] = p
    order[p].append((i, y))
id_num_map = [-1 for i in range(m + 1)]
for i in range(1, n + 1):
    order[i] = list(sorted(order[i], key=lambda x: x[1]))
    for (idx, (city_id, _)) in enumerate(order[i]):
        id_num_map[city_id] = idx + 1
for i in range(1, m + 1):
    print('{:06}{:06}'.format(id_perf_map[i], id_num_map[i]))
