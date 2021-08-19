class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i, j = 0, 0

        max_fruit = 0
        baskets = defaultdict(int)
        while j <= len(tree) and i < len(tree):
            #print(i, j, baskets)
            if j < len(tree) and len(set(list(baskets.keys()) + [tree[j]])) <= 2:
                baskets[tree[j]] += 1
                j += 1
            else:
                baskets[tree[i]] -= 1
                if baskets[tree[i]] == 0:
                    baskets.pop(tree[i])
                i += 1
            max_fruit = max(sum(baskets.values()), max_fruit)
        return max_fruit
