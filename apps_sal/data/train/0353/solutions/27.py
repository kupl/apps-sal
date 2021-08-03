class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = int(1e9 + 7)
        pw = [1]
        for i in range(1, 100001):
            pw.append(pw[-1] * 2 % MOD)
        nums.sort()
        i = 0
        j = len(nums) - 1
        ret = 0
        for i in range(len(nums)):
            while nums[i] + nums[j] > target:
                j -= 1
                if i > j:
                    return ret
            ret += pw[j - i]
            ret %= MOD
        return ret
