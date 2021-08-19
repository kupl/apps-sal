class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        totalBox = len(status)
        gotBoxes = set(initialBoxes)
        # gotKeys = set()
        i = 0
        ans = 0
        visited = set()
        while i < len(initialBoxes):
            boxNow = initialBoxes[i]
            if (boxNow not in visited):
                if (status[boxNow] == 1):
                    visited.add(boxNow)
                    ans += candies[boxNow]
                    # gotKeys |= set(keys[boxNow])
                    # gotBoxes |= set(containedBoxes[boxNow])
                    for newBox in containedBoxes[boxNow]:
                        if status[newBox] == 1:
                            initialBoxes.append(newBox)
                        else:
                            gotBoxes.add(newBox)

                    for keyBox in keys[boxNow]:
                        status[keyBox] = 1
                        if keyBox in gotBoxes:
                            initialBoxes.append(keyBox)
                            gotBoxes.remove(keyBox)
                else:
                    gotBoxes.add(boxNow)
            i += 1
        return ans
