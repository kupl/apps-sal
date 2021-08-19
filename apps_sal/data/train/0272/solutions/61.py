class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        openedBox = set()
        bfs = [i for i in boxes if status[i]]
        while bfs:
            size = len(bfs)
            for _ in range(size):
                box = bfs.pop(0)
                openedBox.add(box)
                for eachContainedBox in containedBoxes[box]:
                    if status[eachContainedBox]:
                        bfs.append(eachContainedBox)
                    boxes.add(eachContainedBox)
                for eachKey in keys[box]:
                    if status[eachKey] == 0 and eachKey in boxes:
                        bfs.append(eachKey)
                    status[eachKey] = 1
        return sum((candies[box] for box in openedBox))
