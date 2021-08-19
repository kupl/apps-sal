class Solution:

    def totalFruit(self, tree: List[int]) -> int:

        def pick(start, end):
            res = 0
            fruitType = set()
            for i in range(start, end):
                fruit = tree[i]
                if fruit not in fruitType and len(fruitType) >= 2:
                    return res
                fruitType.add(fruit)
                res += 1
            return res
        n = len(tree)
        cnt = Counter(tree)
        if len(cnt) <= 2:
            return n
        maxFruit = 0
        for i in range(n):
            maxFruit = max(maxFruit, pick(i, n))
        return maxFruit
