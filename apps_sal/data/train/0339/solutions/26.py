class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq_cnt1 = Counter([x * x for x in nums1])
        sq_cnt2 = Counter([x * x for x in nums2])
        count = 0
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in sq_cnt2:
                    count += sq_cnt2[nums1[i] * nums1[j]]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in sq_cnt1:
                    count += sq_cnt1[nums2[i] * nums2[j]]
        return count
