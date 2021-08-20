class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        m = 0

        def get(val):
            ret = 0
            give = 0
            while val != 0:
                if val & 1:
                    val -= 1
                    ret += 1
                else:
                    val = val // 2
                    give += 1
            return (ret, give)
        for i in range(n):
            if nums[i] == 0:
                continue
            (val, mult) = get(nums[i])
            m = max(m, mult)
            ans += val
        ans += m
        return ans
