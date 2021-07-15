class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_sum(d):
            ans = 0
            for n in nums:
                ans += math.ceil(n/d)
            return ans
        
        l, r = 1, max(nums)
        ans = 0
        
        while l < r:
            m = (l + r) // 2
            test = get_sum(m)
            if test <= threshold:
                ans = m
                r = m
            else:
                l = m + 1
        return l
    

