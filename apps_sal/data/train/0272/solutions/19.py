class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        found_keys = set()
        s = [b for b in initialBoxes if status[b]]
        found_boxes = set([b for b in initialBoxes if not status[b]])
        r = 0
        while s:
            box = s.pop()
            r += candies[box]
            for child in containedBoxes[box]:
                if status[child]:
                    s.append(child)
                else:
                    found_boxes.add(child)
            for key in keys[box]:
                found_keys.add(key)
            opened = found_boxes & found_keys
            for b in opened:
                s.append(b)
            found_boxes -= opened
            found_keys -= opened
        return r
