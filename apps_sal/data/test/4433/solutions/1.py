# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 23:52
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : F1. Spanning Tree with Maximum Degree.py

from collections import defaultdict
from collections import deque


def main():
    n, m = map(int, input().split())

    edge_dict = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        edge_dict[u].append(v)
        edge_dict[v].append(u)

    max_root, max_degree = 0, 0
    for i in range(1, n + 1):
        if len(edge_dict[i]) > max_degree:
            max_root, max_degree = i, len(edge_dict[i])
    # print(max_root, max_degree)

    queue, visit = deque(), set()
    queue.append(max_root)
    visit.add(max_root)

    ret = []
    while queue:
        u = queue.popleft()
        for v in edge_dict[u]:
            if v not in visit:
                visit.add(v)
                queue.append(v)
                ret.append((u, v))
    for u, v in ret:
        print(u, v)


def __starting_point():
    main()


__starting_point()
