class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        self.result_cache = {}

        def f(low, high, nums):
            if low > high:
                return 0
            if low == high:
                return nums[low]
            if (low, high) in self.result_cache:
                return self.result_cache[low, high]
            l = nums[low] + min(f(low + 2, high, nums), f(low + 1, high - 1, nums))
            h = nums[high] + min(f(low + 1, high - 1, nums), f(low, high - 2, nums))
            r = max(l, h)
            self.result_cache[low, high] = r
            return r
        p1 = f(0, len(piles) - 1, piles)
        p2 = sum(piles) - p1
        return p1 > p2
