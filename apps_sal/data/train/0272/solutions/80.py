class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        open = initialBoxes
        x_keys = set()
        locked = set()
        result = 0
        seen = set()
        while len(open) != 0:
            i = open.pop(0)
            if i in seen:
                continue
            for key in keys[i]:
                x_keys.add(key)
            for box in containedBoxes[i]:
                if box in x_keys or status[box] == 1:
                    open.append(box)
                else:
                    locked.add(box)
            for box in locked:
                if box in x_keys:
                    open.append(box)
            result += candies[i]
            seen.add(i)
        return result
