from collections import defaultdict, deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        VALUE_INDEX_MAP = defaultdict(list)
        for (i, v) in enumerate(arr):
            VALUE_INDEX_MAP[v].append(i)
        queue = deque([0])
        seen = set([0])
        nsteps = -1
        while queue:
            levelSize = len(queue)
            nsteps += 1
            for _ in range(levelSize):
                x = queue.popleft()
                if x == len(arr) - 1:
                    return nsteps
                for nx in VALUE_INDEX_MAP[arr[x]] + [x - 1, x + 1]:
                    if 0 <= nx < len(arr) and nx not in seen:
                        queue.append(nx)
                        seen.add(nx)
                VALUE_INDEX_MAP[arr[x]].clear()
        return -1
