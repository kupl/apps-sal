class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = collections.defaultdict(set)
        for i, num in enumerate(nums1):
            set1[num].add(i)
        set2 = collections.defaultdict(set)
        for i, num in enumerate(nums2):
            set2[num].add(i)

        res = 0
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if (nums2[i] * nums2[j]) ** 0.5 == int((nums2[i] * nums2[j]) ** 0.5):
                    m = int((nums2[i] * nums2[j]) ** 0.5)
                    if m in set1:
                        res += len(set1[m])

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if (nums1[i] * nums1[j]) ** 0.5 == int((nums1[i] * nums1[j]) ** 0.5):
                    m = int((nums1[i] * nums1[j]) ** 0.5)
                    if m in set2:
                        res += len(set2[m])
        return res
