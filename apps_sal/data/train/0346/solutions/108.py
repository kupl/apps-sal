class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        l = len(nums)

        def atmost(k):
            res = 0
            cnt = 0
            j = 0
            for i in range(l):
                if nums[i] % 2 == 1:
                    cnt += 1
                while cnt > k:
                    if nums[j] % 2 == 1:
                        cnt -= 1
                    j += 1
                res += i - j + 1
            return res
        return atmost(k) - atmost(k - 1)
