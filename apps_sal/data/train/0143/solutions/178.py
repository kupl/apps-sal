class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        result = 0
        left, right = 0, 0
        basket = collections.defaultdict(int)

        while right < len(tree):
            basket[tree[right]] += 1

            while len(basket) > 2:
                if basket[tree[left]] == 1:
                    basket.pop(tree[left])
                else:
                    basket[tree[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result
