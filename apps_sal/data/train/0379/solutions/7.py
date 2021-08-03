class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = b = i = j = 0

        c = 0
        while(i < len(nums1) or j < len(nums2)):
            if(i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j])):
                a += nums1[i]
                i += 1
            elif(j < len(nums2) and (i == len(nums1) or nums2[j] < nums1[i])):
                b += nums2[j]
                j += 1
            else:
                c += max(a, b) + nums1[i]
                i += 1
                j += 1
                a = b = 0
        return (c + max(a, b)) % (10 ** 9 + 7)
