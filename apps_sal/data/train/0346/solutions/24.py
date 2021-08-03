class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur = res = i = 0
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                k -= 1
                if k == 0:
                    cur = 1
                    while nums[i] % 2 == 0:
                        cur += 1
                        i += 1
                    k += 1
                    i += 1
                    res += cur
            else:
                res += cur
        return res
