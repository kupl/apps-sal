class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        Using sliding window, keep track of the longest window length where unique fruit types <= 2
        the max window will be the answer
        '''
        left = 0
        n = len(tree)
        ans = 0
        basket = set()
        counter = collections.Counter()
        for right, fruit in enumerate(tree):
            basket.add(fruit)
            counter[fruit] += 1
            while len(basket) > 2:
                counter[tree[left]] -= 1
                if counter[tree[left]] == 0:
                    basket.remove(tree[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans

        # # Recursive
        # memo = {}
        # def collect(index, basket=[]):
        #     if index == len(tree):
        #         return 0
        #     # if (index, set(basket))
        #     take = 0
        #     if len(basket) < 2 or (tree[index] in basket):
        #         take = collect(index+1, basket+[tree[index]]) + 1
        #     skip = 0
        #     if len(basket) < 2:
        #         skip = collect(index+1, basket)
        #     return max(take, skip)
        # return collect(0)
