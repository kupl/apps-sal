from collections import Counter


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = Counter()
        max_fr = 0
        i = 0

        for j, t in enumerate(tree):
            baskets[t] += 1

            while len(baskets) > 2:
                baskets[tree[i]] -= 1
                if baskets[tree[i]] == 0:
                    del baskets[tree[i]]

                i += 1

            max_fr = max(max_fr, j - i + 1)

        return max_fr
