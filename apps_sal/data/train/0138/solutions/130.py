class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ans = -10 ** 9

        @lru_cache(None)
        def cal(i):
            nonlocal ans
            if i >= len(nums):
                return [None, None]
            elif nums[i] == 0:
                return [None, None]
            elif nums[i] < 0:
                (pos, neg) = cal(i + 1)
                if neg == None:
                    neg = i
                if pos != None:
                    ans = max(ans, pos - i + 1)
                return [neg, pos]
            else:
                (neg, pos) = cal(i + 1)
                if pos == None:
                    pos = i
                ans = max(ans, pos - i + 1)
                return [neg, pos]
        for i in range(len(nums)):
            cal(i)
        return max(ans, 0)
