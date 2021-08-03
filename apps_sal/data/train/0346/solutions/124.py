class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(K):
            b, e = 0, 0
            ret = 0
            while e < len(nums):
                K -= nums[e] % 2
                while K < 0:
                    K += nums[b] % 2
                    b += 1
                ret += e - b + 1
                e += 1
            return ret
        return atMost(k) - atMost(k - 1)
