import collections
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        square1 = [e ** 2 for e in nums1]
        target1 = collections.Counter(square1)
        for i in range(len(nums2) - 1):
            for j in range(i+1, len(nums2)):
                if nums2[i]*nums2[j] in target1:
                    count += target1[nums2[i]*nums2[j]]
        square2 = [e ** 2 for e in nums2]
        target2 = collections.Counter(square2)
        for i in range(len(nums1) - 1):
            for j in range(i+1, len(nums1)):
                if nums1[i]*nums1[j] in target2:
                    count += target2[nums1[i]*nums1[j]]
        return count
