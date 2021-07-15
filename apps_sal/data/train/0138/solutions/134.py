class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def sgn(x):
            if x < 0:
                return -1
            if x == 0:
                return 0
            return 1
        nums = list(map(sgn, nums))
        def get_ans(start, end):
            # find ans of nums[start: end]
            # nums[start: end] doesn't contain 0
            arr = nums[start: end]
            negative = arr.count(-1)
            result = end - start
            if negative & 1 ^ 1:
                return result
            return result - min(arr.index(-1), arr[::-1].index(-1)) - 1
        
        nums.append(0)
        size = len(nums)
        pair = [0]
        ans = 0
        for i in range(size):
            if nums[i] == 0:
                if not pair:
                    continue
                pair.append(i)
                ans = max(ans, get_ans(*pair))
                pair = [i + 1]
        return ans
