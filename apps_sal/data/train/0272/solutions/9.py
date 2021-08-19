class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        active_set = initialBoxes
        total_candies = 0
        changed = True
        while changed:
            changed = False
            next_active_set = []
            for b in active_set:
                if status[b]:
                    changed = True
                    total_candies += candies[b]
                    for k in keys[b]:
                        status[k] = 1
                    next_active_set += containedBoxes[b]
                else:
                    next_active_set.append(b)
            active_set = next_active_set
        return total_candies

    def SLOWmaxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        open_boxes = set()
        closed_boxes = set()
        for b in initialBoxes:
            if status[b]:
                open_boxes.add(b)
            else:
                closed_boxes.add(b)
        total_candies = 0
        while len(open_boxes) > 0:
            b = open_boxes.pop()
            total_candies += candies[b]
            for key in keys[b]:
                status[key] = 1
                if key in closed_boxes:
                    closed_boxes.remove(key)
                    open_boxes.add(key)
            for bb in containedBoxes[b]:
                if status[bb]:
                    open_boxes.add(bb)
                else:
                    closed_boxes.add(bb)
        return total_candies
