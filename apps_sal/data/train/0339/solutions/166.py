class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (n1, n2) = (Counter(nums1), Counter(nums2))
        rev = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                t = (nums1[i] * nums1[j]) ** (1 / 2)
                if t == int(t) and t in n2:
                    rev += n2[t]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                t = (nums2[i] * nums2[j]) ** (1 / 2)
                if t == int(t) and t in n1:
                    rev += n1[t]
        return rev
