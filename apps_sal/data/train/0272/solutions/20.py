class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        foundBoxes = set(initialBoxes)
        openBoxes = [box for box in foundBoxes if status[box] == 1]
        for i in openBoxes:
            for x in containedBoxes[i]:
                foundBoxes.add(x)
                if status[x] == 1:
                    openBoxes.append(x)
            for x in keys[i]:
                if status[x] == 0 and x in foundBoxes:
                    openBoxes.append(x)
                status[x] = 1
        return sum([candies[i] for i in openBoxes])
