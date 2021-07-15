class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        finalMax = currentMax = last = secondLast = lastCount = 0

        for fruit in tree:
            if fruit == last or fruit == secondLast:
                currentMax += 1
            else:
                currentMax = lastCount + 1

            if fruit == last:
                lastCount += 1
            else:
                secondLast = last
                last = fruit
                lastCount = 1

            finalMax = max(finalMax, currentMax)

        return finalMax


