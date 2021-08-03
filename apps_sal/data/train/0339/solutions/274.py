from math import sqrt


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = [0] * 100001
        count2 = [0] * 100001
        for i in nums1:
            count1[i] += 1
        for i in nums2:
            count2[i] += 1
        m = len(nums1)
        n = len(nums2)
        ans = 0
        for i in range(m - 1):
            for j in range(i + 1, m):
                sq = int(sqrt(nums1[i] * nums1[j]))
                if(sq**2 == nums1[i] * nums1[j]):
                    ans += count2[sq]
        for i in range(n - 1):
            for j in range(i + 1, n):
                sq = int(sqrt(nums2[i] * nums2[j]))
                if(sq**2 == nums2[i] * nums2[j]):
                    ans += count1[sq]
        return ans
