class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        (i, j) = (0, 0)
        (n1, n2) = (len(nums1), len(nums2))
        total1 = 0
        total2 = 0
        while i < n1 or j < n2:
            v1 = nums1[i] if i < n1 else math.inf
            v2 = nums2[j] if j < n2 else math.inf
            if v1 < v2:
                total1 += v1
                i += 1
            elif v2 < v1:
                total2 += v2
                j += 1
            elif v1 == v2:
                total = max(total1 + v1, total2 + v2)
                total1 = total
                total2 = total
                i += 1
                j += 1
        return max(total1, total2) % (10 ** 9 + 7)
