class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        s = [b for b in initialBoxes if status[b]]
        found_boxes = set([b for b in initialBoxes if not status[b]])
        r = 0
        while s:
            box = s.pop()
            r += candies[box]
            for key in keys[box]:
                status[key] = 1
            tbr = set()
            for b in found_boxes:
                if status[b]:
                    s.append(b)
                    tbr.add(b)
            found_boxes -= tbr
            for child in containedBoxes[box]:
                if status[child]:
                    s.append(child)
                else:
                    found_boxes.add(child)
        return r
