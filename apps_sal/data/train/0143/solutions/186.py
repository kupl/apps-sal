class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        fruits = {}
        maxNum = 0
        left = 0
        right = 0
        while right < len(tree):
            while len(fruits) < 3 and right < len(tree):
                fruit = tree[right]
                if fruit not in fruits:
                    fruits[fruit] = 0
                fruits[fruit] += 1
                if len(fruits) < 3:
                    maxNum = max(maxNum, sum(fruits.values()))
                right += 1
            while len(fruits) > 2 and left < right:
                fruit = tree[left]
                fruits[fruit] -= 1
                if fruits[fruit] == 0:
                    del fruits[fruit]
                left += 1
        return maxNum
