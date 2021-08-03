from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        maxAmountOfFruit = 0
        startIndex, endIndex = 0, 0

        countByFruit = defaultdict(int)
        countByFruit[tree[startIndex]] = 1

        while endIndex < len(tree):
            while len(countByFruit) > 2:
                fruitToRemove = tree[startIndex]
                countByFruit[fruitToRemove] -= 1
                if countByFruit[fruitToRemove] == 0:
                    del countByFruit[fruitToRemove]
                startIndex += 1
            maxAmountOfFruit = max(maxAmountOfFruit, endIndex - startIndex + 1)
            endIndex += 1
            if endIndex != len(tree):
                countByFruit[tree[endIndex]] += 1
        return maxAmountOfFruit
