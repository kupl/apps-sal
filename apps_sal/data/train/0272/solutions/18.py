from collections import deque


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        visited = set(initialBoxes)
        reachable = set()
        deq = deque(initialBoxes)
        candy_cnt = 0
        while len(deq) > 0:
            box = deq.popleft()
            candy_cnt += candies[box]
            for cb in containedBoxes[box]:
                reachable.add(cb)
                if cb not in visited and status[cb] == 1:
                    deq.append(cb)
                    visited.add(cb)
            for key in keys[box]:
                status[key] = 1
                if key not in visited and key in reachable:
                    deq.append(key)
                    visited.add(key)
        return candy_cnt
