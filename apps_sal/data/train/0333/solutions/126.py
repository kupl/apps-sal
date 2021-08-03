from collections import defaultdict
from collections import deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pos_m = defaultdict(set)
        for idx, val in enumerate(arr):
            pos_m[val].add(idx)
        visited = [float('inf') for i in range(len(arr))]
        seen = set([0])
        steps = 0
        pos_m[arr[0]].remove(0)

        # (idx, step)
        q = deque()
        q.append((0, 0))
        while q:
            for _ in range(len(q)):
                idx, step = q.popleft()
                if idx == len(arr) - 1:
                    return step
                if idx > 0 and idx - 1 not in seen:
                    seen.add(idx - 1)
                    q.append((idx - 1, step + 1))
                if idx + 1 < len(arr) and idx + 1 not in seen:
                    seen.add(idx + 1)
                    q.append((idx + 1, step + 1))
                for pos in pos_m[arr[idx]]:
                    if pos not in seen:
                        seen.add(pos)
                        q.append((pos, step + 1))
                del pos_m[arr[idx]]

        return -1
