class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total = 0
        boxes = initialBoxes[:]
        locked = []
        while boxes:
            if not any([status[temp] for temp in boxes]):
                break
            box = boxes.pop(0)
            if status[box]:
                total += candies[box]
                for contained in containedBoxes[box]:
                    boxes.append(contained)
                for key in keys[box]:
                    status[key] = 1
            else:
                boxes.append(box)
        return total
