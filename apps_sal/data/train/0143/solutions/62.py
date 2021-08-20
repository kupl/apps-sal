class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        secondLastFruit = -1
        lastFruit = -1
        lastFruitCount = 0
        currFruits = 0
        maxFruits = 0
        for fruit in tree:
            if fruit == lastFruit or fruit == secondLastFruit:
                currFruits += 1
            else:
                currFruits = lastFruitCount + 1
            if fruit == lastFruit:
                lastFruitCount += 1
            else:
                lastFruitCount = 1
                secondLastFruit = lastFruit
                lastFruit = fruit
            maxFruits = max(currFruits, maxFruits)
        return maxFruits
