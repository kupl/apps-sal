# -*- coding: utf-8 -*-

import copy
import queue

N = int(input())
a_list = list(map(int, input().split()))

gain = sum([a for a in a_list if a > 0])

# Flow network
S = 0
T = N + 1
c = [{} for i in range(N + 2)]
for i, a in enumerate(a_list):
    index = i + 1
    if a <= 0:
        c[S][index] = -a
    else:
        c[index][T] = a
    for j in range(index, N + 1, index):
        if not j == index:
            c[index][j] = 10e15

# Residual network
r = copy.deepcopy(c)

# Edmonds-Karp algorithm
max_flow = 0
while True:
    # Find path to T
    q, s, p = queue.Queue(), {S}, None
    q.put((S,))
    findPath = False
    while not q.empty() and not findPath:
        cand_path = q.get(False)
        for to, path in list(r[cand_path[-1]].items()):
            if path == 0:
                continue
            elif to == T:
                p = cand_path + (to,)
                findPath = True
            elif not to in s:
                q.put(cand_path + (to,))
                s.add(to)

    if not findPath:
        break

    # Minimum flow
    min_flow = min([r[p[i]][p[i + 1]] for i in range(len(p) - 1)])
    max_flow += min_flow
    for i in range(len(p) - 1):
        r[p[i]][p[i + 1]] -= min_flow
        if p[i] in r[p[i + 1]]:
            r[p[i + 1]][p[i]] += min_flow
        else:
            r[p[i + 1]][p[i]] = min_flow

print((gain - max_flow))
