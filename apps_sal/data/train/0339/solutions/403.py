from collections import defaultdict


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def get_sq_cnt(nums):
            cnt = defaultdict(int)
            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    cnt[nums[i] * nums[j]] += 1
            return cnt
        (cnt1, cnt2) = (get_sq_cnt(nums1), get_sq_cnt(nums2))
        res = 0
        for num1 in nums1:
            res += cnt2[num1 * num1]
        for num2 in nums2:
            res += cnt1[num2 * num2]
        return res
