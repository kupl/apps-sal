class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = end = disFruits = curTotal = maxTotal = 0
        fruits = {}
        while end < len(tree):
            curFruit = tree[end]
            frontFruit = tree[start]
            if curFruit not in fruits and disFruits == 2:
                if fruits[frontFruit] == 1:
                    del fruits[frontFruit]
                    disFruits -= 1
                else:
                    fruits[frontFruit] -= 1
                curTotal -= 1
                start += 1
            else:
                curFruit = tree[end]
                if curFruit not in fruits:
                    fruits[curFruit] = 1
                    disFruits += 1
                else:
                    fruits[curFruit] += 1
                curTotal += 1
                maxTotal = max(curTotal, maxTotal)
                end += 1
        return maxTotal
