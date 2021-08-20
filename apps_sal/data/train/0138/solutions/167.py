class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        fn = -1
        s = -1
        p = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                fn = -1
                s = -1
                p = 1
            else:
                if s == -1:
                    s = i
                p *= nums[i]
                if p < 0 and fn == -1:
                    fn = i
                if p < 0:
                    ans = max(ans, i - s + 1 - (fn - s + 1))
                elif p > 0:
                    ans = max(ans, i - s + 1)
        return ans
