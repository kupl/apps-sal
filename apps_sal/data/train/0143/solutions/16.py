class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        """
        Using sliding window, keep track of the longest window length where unique fruit types <= 2
        the max window will be the answer
        """
        left = 0
        n = len(tree)
        ans = 0
        basket = set()
        counter = collections.Counter()
        for (right, fruit) in enumerate(tree):
            basket.add(fruit)
            counter[fruit] += 1
            while len(basket) > 2:
                counter[tree[left]] -= 1
                if counter[tree[left]] == 0:
                    basket.remove(tree[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans
