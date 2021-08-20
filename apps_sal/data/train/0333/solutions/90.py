from collections import defaultdict
from collections import deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        indexes = defaultdict(list)
        for (i, v) in enumerate(arr):
            if i == 0 or arr[i - 1] != v:
                indexes[v].append(i)
        queue = deque([(0, True), (len(arr) - 1, False)])
        minimum_steps = {0: 0}
        minimum_steps_negative = {len(arr) - 1: 0}
        while queue:
            (curPos, direction) = queue.popleft()
            if direction and curPos in minimum_steps_negative:
                return minimum_steps_negative[curPos] + minimum_steps[curPos]
            if not direction and curPos in minimum_steps:
                return minimum_steps_negative[curPos] + minimum_steps[curPos]
            candidates = []
            if curPos > 0:
                candidates.append(curPos - 1)
            if curPos < len(arr) - 1:
                candidates.append(curPos + 1)
            candidates.extend(indexes[arr[curPos]])
            ans = []
            for i in candidates:
                if direction:
                    checker = minimum_steps
                else:
                    checker = minimum_steps_negative
                if i not in checker:
                    checker[i] = checker[curPos] + 1
                    queue.append((i, direction))
