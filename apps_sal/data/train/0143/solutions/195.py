class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        max_len = 0
        basket = collections.Counter()
        start = 0
        for (end, fruit) in enumerate(tree):
            basket[fruit] += 1
            while len(basket) >= 3:
                basket[tree[start]] -= 1
                if basket[tree[start]] == 0:
                    del basket[tree[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
