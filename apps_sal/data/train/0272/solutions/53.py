from collections import deque


class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        (seen, queue, result) = ([False] * n, deque(initialBoxes), 0)
        num_locked = 0
        for box in initialBoxes:
            seen[box] = True
        while queue:
            box = queue.popleft()
            if not status[box]:
                queue.append(box)
                num_locked += 1
                if num_locked == len(queue):
                    break
                continue
            num_locked = 0
            result += candies[box]
            for k in keys[box]:
                status[k] = 1
            for cb in containedBoxes[box]:
                if not seen[cb]:
                    queue.append(cb)
                    seen[cb] = True
        return result
