from collections import defaultdict, deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        g = defaultdict(list)
        for (i, n) in enumerate(arr):
            g[n].append(i)
        cur = [0]
        step = 0
        seen = {0}
        while cur:
            nex = []
            for i in cur:
                if i == len(arr) - 1:
                    return step
                for adj in g[arr[i]]:
                    if adj not in seen:
                        seen.add(adj)
                        nex.append(adj)
                g[arr[i]].clear()
                if i - 1 >= 0 and i - 1 not in seen:
                    seen.add(i - 1)
                    nex.append(i - 1)
                if i + 1 < len(arr) and i + 1 not in seen:
                    seen.add(i + 1)
                    nex.append(i + 1)
            step += 1
            cur = nex
        return -1
