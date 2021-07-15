class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMost(m):
            if m < 0:
                return 0
            left = res = 0
            for right, x in enumerate(nums):
                m -= x & 1
                while m < 0:
                    m += nums[left] & 1
                    left += 1
                res += right - left + 1
            return res
        return atMost(k) - atMost(k - 1)
        
        # left = cnt = res = 0
        # for right, x in enumerate(nums):
        #     if x & 1:
        #         k -= 1
        #         cnt = 0
        #     while k == 0:
        #         k += nums[left] & 1
        #         left += 1
        #         cnt += 1
        #     # print(right, cnt)
        #     res += cnt
        # return res
        # def atMost(m):
        #     res = 0
        #     left = 0
        #     for right, x in enumerate(nums):
        #         m -= x & 1
        #         while m < 0:
        #             m += nums[left] & 1
        #             left += 1
        #         res += right - left + 1
        #     return res
        # return atMost(k) - atMost(k-1)

