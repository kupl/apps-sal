from collections import defaultdict, deque
import bisect
from sortedcontainers import SortedList


# class Solution:
#     def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:

#         m = [{} for i in range(n)]
#         for edge, d in zip(edges, succProb):
#             s, e = edge
#             m[s][e] = m[e][s] = d

#         seen = {start: 1}
#         sorted_e = SortedList([m[start][k], k] for k in m[start])

#         while sorted_e:

#             if end in seen: break
#             p, e = sorted_e.pop()
#             seen[e] = p

#             for tmp_e, tmp_p in m[e].items():
#                 if tmp_e in seen: continue
#                 new_p = tmp_p * p
#                 sorted_e.add([new_p, tmp_e])

#         return seen.get(end, 0)

class Solution:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:

        m = [{} for i in range(n)]
        for edge, d in zip(edges, succProb):
            s, e = edge
            m[s][e] = m[e][s] = d

        queue = deque([start])
        seen = [0] * n
        seen[start] = 1

        while queue:

            s = queue.popleft()
            prob = seen[s]

            for e, p in m[s].items():
                tmp = prob * p
                if seen[e] < tmp:
                    seen[e] = tmp
                    queue.append(e)

        return seen[end]
