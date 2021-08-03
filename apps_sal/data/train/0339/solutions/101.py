class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1, dic2 = collections.Counter(nums1), collections.Counter(nums2)
        ans = 0
        m, n = len(nums1), len(nums2)
        for i in range(m):
            for j in range(i + 1, m):
                target = nums1[i] * nums1[j]
                sq = math.sqrt(target)
                if sq * sq == target:
                    ans += dic2[sq]
        for i in range(n):
            for j in range(i + 1, n):
                target = nums2[i] * nums2[j]
                sq = math.sqrt(target)
                if sq * sq == target:
                    ans += dic1[sq]

        return ans
