from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = {0}
        q = deque([(0, 0)])
        val_to_is = defaultdict(list)

        for i, val in enumerate(arr):
            val_to_is[val].append(i)

        def move(i):
            for j in [i - 1, i + 1] + val_to_is[arr[i]]:
                if 0 <= j < len(arr) and j != i and j not in visited:
                    yield j

        while q:
            i, steps = q.pop()
            for j in move(i):
                if j == len(arr) - 1:
                    return steps + 1
                visited.add(j)
                if arr[i] in val_to_is:
                    del val_to_is[arr[i]]
                q.appendleft((j, steps + 1))

        return 0
