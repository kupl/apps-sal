class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        max_count = 1
        basket = {tree[0]: 1}
        i = 0
        for j in range(1, len(tree)):
            basket[tree[j]] = basket.get(tree[j], 0) + 1
            while len(basket) > 2:
                basket[tree[i]] = basket.get(tree[i], 0) - 1
                if basket[tree[i]] == 0:
                    basket.pop(tree[i])
                i += 1
            curr_count = sum(basket.values())
            max_count = max(max_count, curr_count)
        return max_count
