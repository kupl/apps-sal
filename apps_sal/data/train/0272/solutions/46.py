class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        key_set = set()
        box_set = set()
        used = set()
        queue = collections.deque(initialBoxes)
        ans = 0
        while queue:
            box = queue.popleft()
            if box in used:
                continue
            if status[box] == 1 or box in key_set:
                used.add(box)
                if box in key_set:
                    key_set.remove(box)
                if box in box_set:
                    box_set.remove(box)
                ans += candies[box]
                for futureBox in containedBoxes[box]:
                    box_set.add(futureBox)
                for futureKey in keys[box]:
                    key_set.add(futureKey)
                for futureBox in box_set:
                    if futureBox in key_set or status[futureBox] == 1:
                        queue.append(futureBox)
            else:
                box_set.add(box)
        return ans
