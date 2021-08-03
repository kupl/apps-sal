class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        prod = 1
        pos, neg = -1, None
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pos, neg = i, None
                prod = 1
            else:
                prod *= nums[i]
                if prod > 0:
                    ans = max(ans, i - pos)
                else:
                    if neg == None:
                        neg = i
                    ans = max(ans, i - neg)
        return ans
