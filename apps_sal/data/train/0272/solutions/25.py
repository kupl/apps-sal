class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        boxes = []
        unboxes = set()
        for b in initialBoxes:
            if status[b]:
                boxes.append(b)
            else:
                unboxes.add(b)
        visited = set()
        got = 0
        while boxes:
            ns = set()
            for box in boxes:
                if box not in visited:
                    got += candies[box]
                    visited.add(box)
                for key in keys[box]:
                    status[key] |= 1
            for box in boxes:
                for adj in containedBoxes[box]:
                    unboxes.add(adj)
            newBoxes = set()
            for box in unboxes:
                if status[box] and box not in visited:
                    ns.add(box)
                    newBoxes.add(box)
            for box in newBoxes:
                unboxes.remove(box)
            boxes = list(ns)
        return got
