from functools import reduce


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        splitted = sorted(self.split(nums), key=lambda x: len(x), reverse=True)
        v = 0
        for sp in splitted:
            if len(sp) < v:
                break
            v = max(v, self.solve(sp))
        return v

    def split(self, nums):
        prev = None
        ans = []
        hit = False
        for (i, n) in enumerate(nums):
            if n == 0 and prev is not None:
                ans.append(nums[prev:i])
                hit = True
                prev = None
            elif prev is None and n != 0:
                prev = i
        if not hit:
            return [[n for n in nums if n != 0]]
        if prev is not None and prev != len(nums) - 1:
            ans.append(nums[prev:len(nums)])
        return ans

    def solve(self, nums):
        N = len(nums)
        prod = reduce(lambda x, y: x * y, nums, 1)
        if prod > 0:
            return N
        for i in range(N // 2):
            if nums[i] < 0 or nums[N - 1 - i] < 0:
                return N - i - 1
        return 0
