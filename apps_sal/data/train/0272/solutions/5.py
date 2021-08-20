from typing import List
import collections


class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        parent = {}
        used = {}
        ans = 0
        for i in range(len(containedBoxes)):
            used[i] = False
            for box in containedBoxes[i]:
                parent[box] = i
        queue = collections.deque(initialBoxes)
        for box in initialBoxes:
            used[box] = True
        while queue:
            curr_box = queue.popleft()
            ans += candies[curr_box]
            for key in keys[curr_box]:
                status[key] = 1
                if key in parent and used[parent[key]] and (not used[key]):
                    used[key] = True
                    queue.append(key)
            for box in containedBoxes[curr_box]:
                if status[box] and (not used[box]):
                    used[box] = True
                    queue.append(box)
        return ans
