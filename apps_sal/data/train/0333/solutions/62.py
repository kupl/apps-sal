from collections import defaultdict, deque

import heapq


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(set)
        for i, x in enumerate(arr):
            d[x].add(i)
        q, s = [(0, 0)], defaultdict(lambda: float('inf'))
        s[0] = 0
        while q:
            m, i = heapq.heappop(q)
            i = -i
            if i - 1 >= 0 and s[i - 1] > m + 1:
                s[i - 1] = m + 1
                heapq.heappush(q, (m + 1, -(i - 1)))
            if i + 1 < n and s[i + 1] > m + 1:
                if i + 1 == n - 1:
                    return m + 1
                s[i + 1] = m + 1
                heapq.heappush(q, (m + 1, -(i + 1)))
            x, js = arr[i], set()
            for j in d[x]:
                if s[j] > m + 1:
                    if j == n - 1:
                        return m + 1
                    s[j] = m + 1
                    heapq.heappush(q, (m + 1, -j))
                else:
                    js.add(j)
            for j in js:
                d[x].remove(j)
        return s[n - 1]
