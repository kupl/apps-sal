class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        firstFruit = secondFruit = -1
        firstQuant = secondQuant = 0
        ans = 0
        n = len(tree)
        i = 0
        while i < n:
            if firstQuant == 0 or firstFruit == tree[i]:
                firstFruit = tree[i]
                firstQuant += 1
            elif secondQuant == 0 or secondFruit == tree[i]:
                secondFruit = tree[i]
                secondQuant += 1
            elif i > 0 and tree[i - 1] == firstFruit:
                secondFruit = tree[i]
                secondQuant = 1
                j = i - 1
                while j >= 0 and tree[j] == firstFruit:
                    j -= 1
                firstQuant = i - 1 - j
            elif i > 0 and tree[i - 1] == secondFruit:
                firstFruit = tree[i]
                firstQuant = 1
                j = i - 1
                while j >= 0 and tree[j] == secondFruit:
                    j -= 1
                secondQuant = i - 1 - j
            ans = max(ans, firstQuant + secondQuant)
            i += 1
        return ans
