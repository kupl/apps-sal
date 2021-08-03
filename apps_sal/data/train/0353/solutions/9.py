class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()

        i = 0

        j = len(nums) - 1

        result = 0

        mod = 10**9 + 7

        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1

            else:
                sublen = j - i
                result = (result + pow(2, sublen, mod)) % mod
                i += 1

        print(result)

        return result
