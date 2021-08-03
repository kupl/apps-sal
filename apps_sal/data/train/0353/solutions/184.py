class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        right = len(nums) - 1
        count = 0
        # pow2 = [0 for _ in range(len(nums))]
        # pow2[0] = 1
        # for i in range(len(pow2)):
        #     if i>0:
        #         pow2[i] = (pow2[i-1] * 2) % MOD
        for i in range(len(nums)):
            while right >= i and nums[i] + nums[right] > target:
                right -= 1
            if right < i:
                break
            else:
                # count += pow2[right - i]
                count += 2 ** (right - i)
            count %= MOD
        return count % MOD
