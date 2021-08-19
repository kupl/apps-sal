class Solution:
    """
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while True:
            maxv = 0
            for k in range(len(nums)):
                if nums[k] % 2:
                    nums[k] -= 1
                    ans += 1
                maxv = max(maxv, nums[k])
            if maxv == 0:
                break
            if maxv > 0:
                for k in range(len(nums)):
                    nums[k] //= 2
                ans += 1
        return ans
    """

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        shift = 0
        for k in nums:
            strk = bin(k)[2:]
            ans += strk.count('1')
            shift = max(shift, len(strk) - 1)
        return ans + shift
