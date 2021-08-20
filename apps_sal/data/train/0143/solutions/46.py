class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        result = 0
        collected = {}
        i = 0
        for (j, fruit) in enumerate(tree):
            collected[fruit] = collected.get(fruit, 0) + 1
            while len(collected) > 2:
                collected[tree[i]] -= 1
                if not collected[tree[i]]:
                    collected.pop(tree[i])
                i += 1
            result = max(result, j - i + 1)
        return result
