class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = []
        visited = set()
        closedBoxes = set()
        foundedKeys = set()
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                closedBoxes.add(box)
        
        res = 0
        while queue:
            cur = queue.pop(0)
            res += candies[cur]
            for box in containedBoxes[cur]:
                if status[box] == 1:
                    queue.append(box)
                elif (status[box] == 0 and box in foundedKeys):
                    queue.append(box)
                    foundedKeys.remove(box)
                else:
                    closedBoxes.add(box)
            for key in keys[cur]:
                if key in closedBoxes:
                    queue.append(key)
                    closedBoxes.remove(key)
                else:
                    foundedKeys.add(key)
        return res
