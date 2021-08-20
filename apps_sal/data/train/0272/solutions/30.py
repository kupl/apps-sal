class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total_candies = 0
        open_boxes = [box for box in initialBoxes if status[box] == 1]
        locked_boxes = [box for box in initialBoxes if status[box] == 0]
        obtained_keys = set([])
        while len(open_boxes):
            box = open_boxes.pop()
            total_candies += candies[box]
            for key in keys[box]:
                if key in locked_boxes:
                    locked_boxes.remove(key)
                    open_boxes.append(key)
                else:
                    obtained_keys.add(key)
            for cbox in containedBoxes[box]:
                if status[cbox] == 1 or cbox in obtained_keys:
                    open_boxes.append(cbox)
                else:
                    locked_boxes.append(cbox)
        return total_candies
