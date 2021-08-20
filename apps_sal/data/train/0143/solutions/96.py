class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if len(set(tree)) <= 2:
            return len(tree)
        types = set()
        maxFruits = 0
        for i in range(len(tree)):
            start = i
            res = 0
            types = set()
            for i in range(start, len(tree)):
                fruitType = tree[i]
                if len(types) >= 2 and fruitType not in types:
                    break
                elif fruitType in types:
                    res += 1
                else:
                    types.add(fruitType)
                    res += 1
            maxFruits = max(maxFruits, res)
        return maxFruits
