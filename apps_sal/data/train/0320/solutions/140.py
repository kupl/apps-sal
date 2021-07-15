class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        while 1:
            all0 = True
            has_div = False
            for i in range(n):
                if nums[i] == 0:
                    continue
                all0 = False
                if nums[i] & 1:
                    res += 1
                    if nums[i] > 1:
                        has_div = True
                    nums[i] = (nums[i] - 1) // 2
                else:
                    has_div = True
                    nums[i] //= 2
            if all0:
                break
            if has_div:
                res += 1
        return res

