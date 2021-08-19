from functools import lru_cache
from typing import List, Tuple
import numpy
import collections


class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        const_n = len(graph)
        d = collections.defaultdict(list)
        for init in initial:
            vis = set(initial)
            q = collections.deque([init])
            while q:
                index = q.popleft()
                for node in range(len(graph[index])):
                    if graph[index][node] == 0:
                        continue
                    if node in vis:
                        continue
                    vis.add(node)
                    d[node].append(init)
                    q.append(node)
                pass
            pass
        res = [0] * const_n
        for (key, value) in d.items():
            if len(value) == 1:
                res[value[0]] += 1
        if max(res) == 0:
            return min(initial)
        return res.index(max(res))
