from collections import defaultdict


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        st = 0
        max_len = 0
        basket = defaultdict(int)
        for end in range(len(tree)):
            basket[tree[end]] += 1
            while len(basket) > 2:
                basket[tree[st]] -= 1
                if basket[tree[st]] == 0:
                    del basket[tree[st]]
                st += 1
            total = 0
            for k in basket:
                total += basket[k]
            max_len = max(max_len, total)
        return max_len
