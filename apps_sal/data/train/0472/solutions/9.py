from collections import defaultdict, deque


class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        zero_value = set([])

        for i in range(len(arr)):
            if arr[i] == 0:
                zero_value.add(i)

        queue = deque([start])
        seen = set([])
        while queue:
            i = queue.popleft()
            if i in zero_value:
                return True
            seen.add(i)

            up = i + arr[i]
            if up < len(arr) and up not in seen:
                queue.append(up)
            down = i - arr[i]
            if down >= 0 and down not in seen:
                queue.append(down)

        return False
